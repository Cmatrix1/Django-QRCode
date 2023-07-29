from django.views.generic.edit import CreateView
from django.shortcuts import render
from django.views import View
from django.urls import reverse_lazy
from .models import Product
from .forms import ProductForm, ProductDeleteForm


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/product_create.html' 
    success_url = '/'


class ProductDeleteView(View):
    model = Product
    template_name = 'products/product_delete.html'
    success_url = '/'

    def get(self, request):
        return render(request, self.template_name, context={"form":ProductDeleteForm()})
    
    def post(self, request):
        form = ProductDeleteForm(request.POST)
        deleted = False
        if form.is_valid():
            qrcode = form.cleaned_data.get("qrcode")
            try:
                self.model.objects.get(qrcode=qrcode).delete()
                deleted = True
            except:
                pass
        return render(request, self.template_name, context={"deleted":deleted})
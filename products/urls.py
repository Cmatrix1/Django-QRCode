from django.urls import path
from .views import ProductCreateView, ProductDeleteView

app_name = "products"

urlpatterns = [
    path('create/', ProductCreateView.as_view(), name='product_create'),
    path('delete/', ProductDeleteView.as_view(), name='product_delete'),
]

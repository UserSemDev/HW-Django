from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import home, contacts, product_info, add_product, products_page

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('<int:pk>', products_page, name='products_page'),
    path('contacts/', contacts, name='contacts'),
    path('product/<int:pk>', product_info, name='product_info'),
    path('add_product/', add_product, name='add_product'),
]

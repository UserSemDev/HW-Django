from django.urls import path

from catalog.views import home, contacts, product_info, add_product, products_page

urlpatterns = [
    path('', home),
    path('<int:pk>', products_page),
    path('contacts/', contacts),
    path('product/<int:pk>', product_info),
    path('add_product/', add_product),
]

from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import ProductListView, HomeIndexView, ProductDetailView, \
    ProductCreateView, ContactCreateView, ProductUpdateView, ProductDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path('', HomeIndexView.as_view(), name='home_page'),
    path('contacts/', ContactCreateView.as_view(), name='index_contact'),
    path('products/', ProductListView.as_view(), name='product_list'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('product/update/<int:pk>', ProductUpdateView.as_view(), name='product_update'),
    path('product/delete/<int:pk>', ProductDeleteView.as_view(), name='product_delete')
]

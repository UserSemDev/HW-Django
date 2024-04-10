from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import ProductListView, HomeIndexView, ProductDetailView, \
    ProductCreateView, ContactIndexView

app_name = CatalogConfig.name

urlpatterns = [
    path('', HomeIndexView.as_view(), name='home_page'),
    path('contacts/', ContactIndexView.as_view(), name='index_contact'),
    path('products/', ProductListView.as_view(), name='list_product'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='detail_product'),
    path('create/', ProductCreateView.as_view(), name='create_product'),
]

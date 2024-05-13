from django.urls import path
from django.views.decorators.cache import cache_page, never_cache

from catalog.apps import CatalogConfig
from catalog.views import ProductListView, HomeIndexView, ProductDetailView, \
    ProductCreateView, ContactCreateView, ProductUpdateView, ProductDeleteView, CategoryListView, CategoryDetailView

app_name = CatalogConfig.name

urlpatterns = [
    path('', HomeIndexView.as_view(), name='home_page'),
    path('contacts/', ContactCreateView.as_view(), name='index_contact'),
    path('products/', ProductListView.as_view(), name='product_list'),
    path('product/<int:pk>', cache_page(60)(ProductDetailView.as_view()), name='product_detail'),
    path('product/create/', never_cache(ProductCreateView.as_view()), name='product_create'),
    path('product/update/<int:pk>', never_cache(ProductUpdateView.as_view()), name='product_update'),
    path('product/delete/<int:pk>', never_cache(ProductDeleteView.as_view()), name='product_delete'),
    path('category/', CategoryListView.as_view(), name='categories'),
    path('category/<int:pk>', CategoryDetailView.as_view(), name='category_detail')
]

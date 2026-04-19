from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryV, ProductV
from .views import productlist, search

router=DefaultRouter()
router.register(r'categories', CategoryV)
router.register(r'products', ProductV)

urlpatterns = [
    path('',include(router.urls)),
    path('products-list/', productlist, name='product_list'),
    path('products/search/', search, name='product_search'),
]

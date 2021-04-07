from django.conf.urls import url

from django.urls import path, re_path
re_path

from api.views import product_detail, product_list, category_list, category_detail, hello

urlpatterns = [

    path('hi/', hello),
    path('products/', product_list),
    path('products/<int:product_id>/', product_detail),
    path('categories/', category_list),
    path('categories/<int:category_id>/', category_detail)
]

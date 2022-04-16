
from django.contrib import admin
from django.urls import path
from Products.views import index,category,product



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name = 'index'),
    path('category/<id>/', category, name='category'),
    path('product/<id>/', product, name='product'),
]

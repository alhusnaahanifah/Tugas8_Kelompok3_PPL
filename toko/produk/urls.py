from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('kontak/', views.kontak, name='kontak'),
    path('produk/<int:id>/', views.produk_detail, name='produk-detail'),
    path('produk/', views.daftar_produk, name='daftar_produk'),
]
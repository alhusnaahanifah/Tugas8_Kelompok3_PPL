from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("Selamat datang di toko online!")

def kontak(request):
    return HttpResponse("Hubungi kami di email@example.com")


def produk_detail(request, id):
    return HttpResponse(f"Menampilkan produk dengan ID: {id}")

def daftar_produk(request):
  return render(request, 'daftar_produk.html')

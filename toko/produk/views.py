from django.shortcuts import render
from django.http import HttpResponse

# Data produk disimpan di luar fungsi, supaya bisa diakses dari semua view
products = [
    {
        "id": 1,
        "name": "Laptop Asus Vivobook 14",
        "price": 7500000,
        "description": "Laptop ringan dan bertenaga untuk kebutuhan harian dan kuliah.",
        "stock": 15
    },
    {
        "id": 2,
        "name": "Smartphone Samsung Galaxy A54",
        "price": 4999000,
        "description": "Smartphone dengan kamera jernih dan performa baterai kuat.",
        "stock": 25
    },
    {
        "id": 3,
        "name": "Headphone Sony WH-1000XM4",
        "price": 3999000,
        "description": "Headphone wireless premium dengan fitur noise-cancelling terbaik.",
        "stock": 20
    },
    {
        "id": 4,
        "name": "Smartwatch Amazfit GTR 4",
        "price": 2799000,
        "description": "Jam tangan pintar dengan pelacak kesehatan dan GPS akurat.",
        "stock": 30
    },
    {
        "id": 5,
        "name": "Keyboard Logitech G Pro X",
        "price": 1899000,
        "description": "Keyboard mekanikal profesional dengan switch yang dapat diganti.",
        "stock": 18
    },
    {
        "id": 6,
        "name": "Mouse Logitech MX Master 3",
        "price": 1450000,
        "description": "Mouse ergonomis untuk produktivitas tinggi dan desain elegan.",
        "stock": 22
    },
    {
        "id": 7,
        "name": "Monitor Samsung 27 Inch Curved",
        "price": 3299000,
        "description": "Monitor melengkung Full HD untuk pengalaman visual imersif.",
        "stock": 10
    },
    {
        "id": 8,
        "name": "Speaker Bluetooth JBL Flip 5",
        "price": 1800000,
        "description": "Speaker portabel tahan air dengan suara bertenaga dan jernih.",
        "stock": 16
    },
    {
        "id": 9,
        "name": "Tablet Apple iPad 9th Gen",
        "price": 5999000,
        "description": "Tablet powerful untuk multitasking, belajar, dan hiburan.",
        "stock": 12
    },
    {
        "id": 10,
        "name": "Powerbank Anker 20000mAh",
        "price": 600000,
        "description": "Powerbank berkapasitas besar dengan teknologi fast-charging.",
        "stock": 35
    }
]

def index(request):
    return render(request, 'home.html')

def kontak(request):
    return render(request, 'kontak.html')

def daftar_produk(request):
    return render(request, 'daftar_produk.html', {'products': products})

def produk_detail(request, id):
    # Cari produk berdasarkan id
    produk = next((item for item in products if item["id"] == id), None)
    if produk is None:
        return HttpResponse("Produk tidak ditemukan.", status=404)
    return render(request, 'produk_detail.html', {'produk': produk})

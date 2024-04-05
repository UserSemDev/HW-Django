import math

from django.shortcuts import render
from catalog.models import Product, Contact, Category


def home(request):
    list_product = Product.objects.all()
    context = {
        "objects_list": list_product,
        "title": 'Главная'
    }

    return render(request, 'catalog/home.html', context)


def products_page(request, pk):
    list_product = Product.objects.all()
    count_page_product = math.ceil(len(list_product) / 4)

    context = {
        'objects_list': list_product[(pk*4-4):(pk*4)],
        'title': 'Продукты',
        'prev_url': f'/{pk-1 if pk-1 else 1}',
        'next_url': f'/{pk+1 if pk < count_page_product else count_page_product}',
    }
    return render(request, 'catalog/home.html', context)


def contacts(request):
    context = {
        "object": Contact.objects.get(pk=1),
        "title": 'Контакты'
    }
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'Имя: {name} | Телефон: {phone} | Сообщение: {message}')
    return render(request, 'catalog/contacts.html', context)


def product_info(request, pk):
    context = {
        'object': Product.objects.get(pk=pk),
        'title': 'Продукт'
    }
    return render(request, 'catalog/product.html', context)


def add_product(request):
    context = {
        'objects_list': Category.objects.all(),
        'title': 'Добавление товара'
    }
    if request.method == 'POST':
        print(request.POST)
        print(request.FILES)
        print(request.POST.get('category'))
        Product.objects.create(
            pk=len(Product.objects.all()) + 1,
            name=request.POST.get('name'),
            description=request.POST.get('description'),
            image=request.FILES.get('image'),
            category=Category.objects.get(pk=request.POST.get('category')),
            price=request.POST.get('price'),
        )
    return render(request, 'catalog/add_product.html', context)

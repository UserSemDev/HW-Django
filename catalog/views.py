import math
import os

from django.core.files.uploadedfile import InMemoryUploadedFile
from django.shortcuts import render
from catalog.models import Product, Contact, Category


def home(request):
    list_product = Product.objects.all()[:8]

    context = {
        "objects_list": list_product,
        "title": 'Главная',
        "start_page": '1',
    }

    return render(request, 'catalog/home.html', context)


def products_page(request, pk):
    list_product = Product.objects.all()
    count_page_product = math.ceil(list_product.count() / 4)
    prev_url = f'{pk-1 if pk != 1 else "/"}'
    next_url = f'{pk+1 if pk != count_page_product else "/"}'
    context = {
        'objects_list': list_product[(pk*4-4):(pk*4)],
        'title': 'Продукты',
        'prev_url': prev_url,
        'next_url': next_url,
    }
    if prev_url == "/":
        context['prev_disabled'] = 'disabled'
    if next_url == "/":
        context['next_disabled'] = 'disabled'

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
        image = request.FILES.get('image')

        obj_image = InMemoryUploadedFile(
            image.file, 'image', f'{Product.objects.count() + 1:04}_{image.name}',
            image.content_type, image.tell, image.charset)

        Product.objects.create(
            name=request.POST.get('name'),
            description=request.POST.get('description'),
            image=obj_image,
            category_id=request.POST.get('category'),
            price=request.POST.get('price'),
        )

    return render(request, 'catalog/add_product.html', context)

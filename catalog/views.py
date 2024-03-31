from django.shortcuts import render

from catalog.models import Product, Contact


def home(request):
    products = Product.objects.all()
    for num, item in enumerate(products[:5], 1):
        print(f"{num}: {item}")
    return render(request, 'catalog/home.html', context={"products": products})


def contacts(request):
    contact = Contact.objects.get(pk=1)
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'Имя: {name} | Телефон: {phone} | Сообщение: {message}')
        user_data = {"name": name,
                     "phone": phone,
                     "message": message}

        return render(request, 'catalog/contacts.html',
                      context={"user_data": user_data, "contact": contact})
    else:
        return render(request, 'catalog/contacts.html', context={"contact": contact})
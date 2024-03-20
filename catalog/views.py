from django.shortcuts import render


def home(request):
    return render(request, 'catalog/home.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'Имя: {name} | Телефон: {phone} | Сообщение: {message}')
        user_input = {"name": name,
                      "phone": phone,
                      "message": message
                      }
        return render(request, 'catalog/contacts.html', context={"data": user_input})
    return render(request, 'catalog/contacts.html')
from django.urls import reverse_lazy
from django.views.generic import TemplateView, DetailView, CreateView, ListView
from catalog.models import Product, Contact, Category, Feedback


class HomeIndexView(TemplateView):
    template_name = 'catalog/index.html'
    extra_context = {
        "title": "Главная",
    }

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['objects_list'] = Product.objects.all()[:8]
        return context_data


class ContactCreateView(CreateView):
    model = Feedback
    fields = ('name', 'phone', 'message')
    extra_context = {
        "title": 'Контакты'
    }

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['object'] = Contact.objects.get(pk=1)
        return context_data

    def form_valid(self, form):
        if form.is_valid():
            form.save()
        return super().form_valid(form)

    success_url = reverse_lazy('catalog:index_contact')


class ProductListView(ListView):
    paginate_by = 4
    model = Product
    extra_context = {
        "title": "Продукты"
    }


class ProductDetailView(DetailView):
    model = Product
    extra_context = {
        "title": "Продукт"
    }


class ProductCreateView(CreateView):
    model = Product
    fields = ('name', 'description', 'image', 'category', 'price')
    extra_context = {
        "title": "Добавление товара"
    }

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['objects_list'] = Category.objects.all()
        return context_data

    def form_valid(self, form):
        if form.is_valid():
            instance = form.save(commit=False)
            instance.image.name = f'{Product.objects.count() + 1:04}_{form.cleaned_data["image"].name}'
            instance.save()
        return super().form_valid(form)

    success_url = reverse_lazy('catalog:list_product')

from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, DetailView, CreateView, ListView, UpdateView, DeleteView

from catalog.forms import ProductForms
from catalog.models import Product, Contact, Category, Feedback, Version


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

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['version'] = Version.objects.filter(product=self.object)
        print(context_data)
        return context_data


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForms
    extra_context = {
        "title": "Добавление товара"
    }
    success_url = reverse_lazy('catalog:product_list')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['objects_list'] = Category.objects.all()
        return context_data

    def form_valid(self, form):
        if form.is_valid():
            instance = form.save(commit=False)
            instance.image.name = f'{Product.objects.count() + 1:04}_{instance.image.name}'
            instance.save()
        return super().form_valid(form)


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForms
    extra_context = {
        "title": "Редактирование товара"
    }

    def get_success_url(self):
        return reverse('catalog:product_detail', args=[self.kwargs.get('pk')])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['objects_list'] = Category.objects.all()
        return context_data

    def form_valid(self, form):
        if form.is_valid():
            instance = form.save(commit=False)
            if instance.image:
                instance.image.name = f'{Product.objects.count():04}_{instance.image.name}'
            instance.save()
        return super().form_valid(form)


class ProductDeleteView(DeleteView):
    model = Product
    extra_context = {
        "title": "Удаление товара"
    }
    success_url = reverse_lazy('catalog:product_list')

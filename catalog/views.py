from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.forms import inlineformset_factory
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, DetailView, CreateView, ListView, UpdateView, DeleteView

from catalog.forms import ProductForm, VersionForm, VersionFormSet, ProductModeratorForm
from catalog.models import Product, Contact, Feedback, Version, Category
from catalog.services import get_categories_from_cache, get_products_from_cache


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


class CategoryListView(LoginRequiredMixin, ListView):
    model = Category
    extra_context = {
        "title": "Категории продуктов"
    }

    def get_queryset(self):
        return get_categories_from_cache()


class CategoryDetailView(LoginRequiredMixin, DetailView):
    model = Category

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = f"Категория {self.object}"
        context_data['objects_list'] = Product.objects.filter(category=self.kwargs.get('pk'))
        return context_data


class ProductListView(ListView):
    paginate_by = 4
    model = Product
    extra_context = {
        "title": "Продукты"
    }

    def get_queryset(self):
        return get_products_from_cache()


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    extra_context = {
        "title": "Продукт"
    }

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['version'] = self.object.version.filter(is_active=True).first()
        return context_data


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    extra_context = {
        "title": "Добавление товара"
    }
    success_url = reverse_lazy('catalog:product_list')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        if form.is_valid() and formset.is_valid():
            self.object = form.save()
            self.object.owner = self.request.user
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form, formset=formset))


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    extra_context = {
        "title": "Редактирование товара"
    }

    def get_success_url(self):
        return reverse('catalog:product_detail', args=[self.kwargs.get('pk')])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, formset=VersionFormSet, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        if form.is_valid() and formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form, formset=formset))

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner or user.is_superuser:
            return ProductForm
        if user.has_perms(['catalog.can_change_category',
                           'catalog.can_change_description',
                           'catalog.set_published_status']):
            return ProductModeratorForm

    def dispatch(self, request, *args, **kwargs):
        user = self.request.user
        if (user != self.get_object().owner and not user.is_superuser and
                not user.groups.filter(name='Moderator').exists()):
            raise PermissionDenied

        return super().dispatch(request, *args, **kwargs)


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    extra_context = {
        "title": "Удаление товара"
    }
    success_url = reverse_lazy('catalog:product_list')

    def dispatch(self, request, *args, **kwargs):
        user = self.request.user
        if user != self.get_object().owner and not user.is_superuser:
            raise PermissionDenied

        return super().dispatch(request, *args, **kwargs)

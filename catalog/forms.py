from django import forms
from django.forms import BooleanField

from catalog.models import Product, Version

FORBIDDEN_WORDS = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fields_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = "form-check-input"
            else:
                field.widget.attrs['class'] = "form-control"


class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('created_at', 'updated_at', )

    def clean_name(self):
        clean_data = self.cleaned_data.get('name')
        for word in FORBIDDEN_WORDS:
            if word in clean_data.lower():
                raise forms.ValidationError(f'В названии продукта содержится запрещенное слово: {word}')
        return clean_data


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        exclude = '__all__'

    def clean_description(self):
        clean_data = self.cleaned_data.get('description')
        for word in FORBIDDEN_WORDS:
            if word in clean_data.lower():
                raise forms.ValidationError(f'В описании сезона содержится запрещенное слово: {word}')
        return clean_data

    # def clean_is_active(self):
    #     is_active = self.cleaned_data.get('is_active')
    #     product = self.cleaned_data.get('product')
    #     active_versions = Version.objects.filter(product=product, is_active=True).exists()
    #     if is_active and active_versions:
    #         raise forms.ValidationError('Можно выбрать только один активный сезон')
    #     return is_active
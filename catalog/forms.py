from django import forms
from django.core.exceptions import ValidationError
from django.forms import BooleanField, BaseInlineFormSet

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
        exclude = ('created_at', 'updated_at', 'owner',)

    def clean_name(self):
        clean_data = self.cleaned_data.get('name')
        for word in FORBIDDEN_WORDS:
            if word in clean_data.lower():
                raise forms.ValidationError(f'В названии продукта содержится запрещенное слово: {word}')
        return clean_data


class ProductModeratorForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = ('category', 'description', 'is_published',)

    def clean_name(self):
        clean_data = self.cleaned_data.get('name')
        for word in FORBIDDEN_WORDS:
            if word in clean_data.lower():
                raise forms.ValidationError(f'В названии продукта содержится запрещенное слово: {word}')
        return clean_data


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        exclude = ('product', )

    def clean_description(self):
        clean_data = self.cleaned_data.get('description')
        for word in FORBIDDEN_WORDS:
            if word in clean_data.lower():
                raise forms.ValidationError(f'В описании сезона содержится запрещенное слово: {word}')
        return clean_data


class VersionFormSet(BaseInlineFormSet):
    def clean(self):
        super().clean()
        active_version = [form.cleaned_data for form in self.forms if form.cleaned_data.get('is_active')]
        if len(active_version) > 1:
            raise ValidationError('Можно выбрать только один активный сезон')
        return active_version

from django import forms

from catalog.models import Product


class ProductForms(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('created_at', 'updated_at', )

    def clean_name(self):
        clean_data = self.cleaned_data.get('name')
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево',
                           'бесплатно', 'обман', 'полиция', 'радар']
        for word in forbidden_words:
            if word in clean_data.lower():
                raise forms.ValidationError(f'В названии продукта содержится запрещенное слово: {word}')
        return clean_data

from django import forms
from .models import product


class productForm(forms.ModelForm):

    class Meta:
        model = product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        products = product.objects.all()

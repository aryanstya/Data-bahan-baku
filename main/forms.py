from django.forms import ModelForm
from main.models import dataBahan

class ProductForm(ModelForm):
    class Meta:
        model = dataBahan
        fields = ["name", "amount", "description"]
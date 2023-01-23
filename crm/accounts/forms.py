from django.forms import ModelForm
from .models import Order

class OrderForm(ModelForm):
    class Meta:
        model = Order # Which model we built form for
        fields = '__all__'  # If we want use only selected fields then use list ex. ['customer', 'product'].

from django.forms import ModelForm
from orders.models import Order, Product

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = [
            'name',
            'budget',
            'courier',
            'description',
            'create_date',
            'change_date',
            'creator',
            'stage',
            'responsible',
            'address',
            'client_FIO',
            'client_phone',
            'product'
        ]
        exclude = ['creator', 'create_date', 'change_date', 'company', 'source']

class ProdutForm(ModelForm):
    class Meta:
        model = Product
        fields = [   
            'name',
            'among',
            'price_per_piece',
        ]
from django.forms import ModelForm

from .models import Courier

class CourierForm(ModelForm):
    class Meta:
        model = Courier
        fields = [
            'name',
            'surname',
            'phone_number',
            'telegram_name',
            'available_regions',
            'telegram_chat_id',
            'isActive',
        ]
        exclude = ['telegram_chat_id',]

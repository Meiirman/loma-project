from django.forms import ModelForm

from core.models import CustomBackground


class CustomBackgroundForm(ModelForm):
    class Meta:
        model = CustomBackground
        fields = [   
            'user',
            'background'
        ]
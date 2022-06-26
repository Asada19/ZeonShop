from .models import Callback
from django.forms import ModelForm
from django import forms
 
class CallbackForm(ModelForm):
    class Meta:
        model = Callback
        fields = ['name', 'phone']       
        def __init__(self, *args, **kwargs):
            super(CallbackForm, self).__init__(*args, **kwargs)

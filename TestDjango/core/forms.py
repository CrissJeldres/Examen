from pyexpat import model
from django.forms import ModelForm
from .models import *

class stockForm(ModelForm):
    class Meta:
        model = stock
        fields = ['cod','nombre','cantidad','precio']

class compraForm(ModelForm):
    class Meta:
        model = compra
        fields = ['compra','producto','precio','cantidad']

        

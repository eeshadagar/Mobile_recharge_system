from django import forms
from .models import postrecharge

CHOICES =(
    ("jio", "Jio"),
    ("BSNL", "BSNL"),
    ("Airtel", "Airtel"),
    ("Idea", "Idea"),
    ("Vodafone", "Vodafone"),
)

class PostRechargeForm(forms.ModelForm):
    number = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    operator = forms.ChoiceField(choices = CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    region = forms.CharField(max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    

    class Meta:
        model = postrecharge
        fields = ('number','operator', 'region')
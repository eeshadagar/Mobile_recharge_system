from django import forms
from main_app.models import Detail

CHOICES =(
    ("jio", "Jio"),
    ("BSNL", "BSNL"),
    ("Airtel", "Airtel"),
    ("Idea", "Idea"),
    ("Vodafone", "Vodafone"),
)

class RechargeForm(forms.ModelForm):
    number = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    amount = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    operator = forms.ChoiceField(choices = CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Detail
        fields = ('number', 'amount', 'operator')
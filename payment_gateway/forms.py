from django import forms
from .models import Payments_post, Payments_pre
from django.core.exceptions import ValidationError

class PaymentForm_pre(forms.ModelForm):
    amount = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder':'Enter the amount'}))
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'abc'}))
    number = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder':'0000 0000 0000 0000'}))
    expirey = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'00/00'}))
    cvv = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder':'000'}))

    class Meta:
        model = Payments_pre
        fields = ('amount','name', 'number', 'expirey', 'cvv')

    def clean(self):
        cleaned_data = super().clean()
        data = cleaned_data.get('number')
        expiry = cleaned_data.get('expirey')
        cvv = cleaned_data.get('cvv')
        lennn = len(str(cvv))
        lenn = len(str(data))
        a = len(expiry)
        if (lenn != 12):
            raise ValidationError('card number is not valid')
        elif (lennn != 3):
            raise ValidationError('cvv is not valid')
        elif (a!=5 and '!' not in expiry ):
            raise ValidationError('expiry date is not valid')
        return cleaned_data

class PaymentForm_post(forms.ModelForm):
    amount = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder':'Enter the amount'}))
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'abc'}))
    number = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder':'0000 0000 0000 0000'}))
    expirey = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'00/00'}))
    cvv = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder':'000'}))

    class Meta:
        model = Payments_post
        fields = ('amount','name', 'number', 'expirey', 'cvv')
    
    def clean(self):
        cleaned_data = super().clean()
        data = cleaned_data.get('number')
        expiry = cleaned_data.get('expirey')
        cvv = cleaned_data.get('cvv')
        lennn = len(str(cvv))
        lenn = len(str(data))
        a = len(expiry)
        if (lenn != 12):
            raise ValidationError('card number is not valid')
        elif (lennn != 3):
            raise ValidationError('cvv is not valid')
        elif (a!=5 and '!' not in expiry ):
            raise ValidationError('expiry date is not valid')
        return cleaned_data

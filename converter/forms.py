from django import forms
import requests


response = requests.get(url='https://v6.exchangerate-api.com/v6/e0c099404baec334a56e3cb4/latest/USD').json()
currencies = response.get('conversion_rates')
currency_choices = [(currency, currency) for currency in currencies]


class ConverterForm(forms.Form):
    currency_from = forms.ChoiceField(choices=currency_choices, label='From Currency')
    amount = forms.FloatField(label='Amount', widget=forms.NumberInput(attrs={'placeholder': 'Введите сумму'}))
    currency_to = forms.ChoiceField(choices=currency_choices, label='To Currency')

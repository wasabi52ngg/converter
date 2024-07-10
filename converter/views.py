from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from django.views import View
from .forms import ConverterForm
import requests


def get_currency_equality(currency_from: str, currency_to: str):
    response = requests.get(url='https://v6.exchangerate-api.com/v6/e0c099404baec334a56e3cb4/latest/USD').json()
    currencies = response.get('conversion_rates')
    return currencies.get(currency_to) / currencies.get(currency_from)


class MainPageView(View):

    def get(self, request):
        form = ConverterForm()
        return render(request, 'converter/home_page.html', context={'form': form})

    def post(self, request):
        form = ConverterForm(request.POST)
        if form.is_valid():
            currency_from = str(form.cleaned_data['currency_from'])
            currency_to = form.cleaned_data['currency_to']
            amount = form.cleaned_data['amount']
            result = round(amount * get_currency_equality(currency_from, currency_to), 2)
            return render(request, 'converter/home_page.html', context={'result': result, 'form': form})
        return render(request, 'converter/home_page.html', context={'form': form})

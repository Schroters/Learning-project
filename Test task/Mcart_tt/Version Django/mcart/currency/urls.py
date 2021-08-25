from django.urls import path
from . import views
from . import views_currency_character_code, views_exchange_rate


urlpatterns = [
    path('', views.index, name='home'),
    path('currency_list', views_currency_character_code.currency_list, name='currency_list'),
    path('exchange_rate', views_exchange_rate.exchange_rate, name='exchange_rate'),
]

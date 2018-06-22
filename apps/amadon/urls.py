from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^amadon/$',views.index, name='index'),### home page
    url(r'^amadon/buy$', views.buy, name='process'), ###form from home went to buy
    url(r'^amadon/checkout$', views.checkout, name='checkout'), #
    url(r'^amadon/clear$', views.clearcart, name='clearcart')
]

# home display

# user buy:
# use dictionary to mapping item id and price

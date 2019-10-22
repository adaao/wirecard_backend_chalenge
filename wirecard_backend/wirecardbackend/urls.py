from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^clients/$', views.ClientList.as_view(), name='client-list'),
    url(r'^buyer/$', views.BuyerList.as_view(), name='buyer-list'),
    url(r'^card/$', views.CardList.as_view(), name='card-list'),
    url(r'^payment/$', views.PaymentList.as_view(), name='payment-list'),

]
from django.shortcuts import render
from rest_framework import generics
from . import models
from . import serializers

class ClientList(generics.ListCreateAPIView):
    queryset = models.Client.objects.all()
    serializer_class = serializers.ClientSerializer

class BuyerList(generics.ListCreateAPIView):
    queryset = models.Buyer.objects.all()
    serializer_class = serializers.BuyerSerializer

class PaymentList(generics.ListCreateAPIView):
    queryset = models.Payment.objects.all()
    serializer_class = serializers.PaymentSerializer

class CardList(generics.ListCreateAPIView):
    queryset = models.Card.objects.all()
    serializer_class = serializers.CardSerializer


from django.db import models
from creditcards.models import CardExpiryField

class Client(models.Model):
    id = models.AutoField(primary_key=True) 


    def __srt__(self):
        return self.id


class Buyer(models.Model) :
    Name = models.CharField(max_length=200)
    Email = models.EmailField(max_length=200)
    CPF = models.CharField(max_length=11)


    def __srt__(self):
        return self.Name


class Payment(models.Model):
    payment_types = [(1, 'Boleto'), (2, 'Cartão')]
    
    Amount = models.DecimalField(max_digits=10, decimal_places=2)
    Type = models.CharField(max_length=1, choices=payment_types)
    Card = models.ForeignKey('Card', on_delete=models.CASCADE, null=True)


    def __srt__(self):
        return (self.Amount, self.Type)


class Card(models.Model):
    holder_name = models.CharField(max_length=200)
    number = models.CharField(max_length=16)
    expiration_date = CardExpiryField(('expiration date'))
    CVV = models.IntegerField()


    def __srt__(self):
        return self.number


from django.db import models
from creditcards.models import CardExpiryField

class Client(models.Model):
    client_status = [(1, 'Ativo'), (0, 'Inativo')]
    
    id = models.AutoField(primary_key = True)
    is_active = models.BooleanField(choices = client_status, null = False)

    def __srt__(self):
        return self.id


class Buyer(models.Model) :
    name = models.CharField(max_length = 200)
    email = models.EmailField(max_length = 200)
    cpf = models.CharField(max_length = 11)

    class Meta:
        db_table = 'buyer'

    def __srt__(self):
        return self.name


class Payment(models.Model):
    payment_types = [(1, 'Boleto'), (2, 'Cartão')]
    payment_status = [(1, 'Finalizado'), (0, 'Aguardando pagamento')]

    client_id = models.ForeignKey('Client', on_delete = models.CASCADE, null = False)
    amount = models.DecimalField(max_digits = 10, decimal_places = 2)
    type = models.CharField(max_length=1, choices = payment_types)
    card = models.ForeignKey('Card', on_delete = models.CASCADE, null = True)
    boleto_number = models.IntegerField(null = True)
    payment_status = models.BooleanField(choices = payment_status, null = False)


    def __srt__(self):
        return (self.amount, self.type)


class Card(models.Model):
    holder_name = models.CharField(max_length = 200)
    number = models.CharField(max_length = 16)
    expiration_date = CardExpiryField(('expiration date'))
    cvv = models.IntegerField()


    def __srt__(self):
        return self.number


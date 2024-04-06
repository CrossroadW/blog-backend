from django.db import models


# Create your models here.
class Person(models.Model):
    CHOICES_GENDER = (
        (1, '男'), (2, '女'),
    )
    name = models.CharField(max_length=125)
    age = models.IntegerField()
    gender = models.BooleanField(choices=CHOICES_GENDER)
    id_card = models.CharField(max_length=18)
    address = models.CharField(max_length=255)
    temperature = models.DecimalField(max_digits=4,decimal_places=2)

    class Meta:
        permissions = ()

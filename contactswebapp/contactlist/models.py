from django.conf import settings
from django.db import models
from django.utils import timezone


class Contact (models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    phone_number = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
   
    def __str__(self):
        return self.full_name

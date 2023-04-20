from django.db import models
# from django.core.urlresolvers import reverse
from django.urls import reverse

# Create your models here.

class Company(models.Model):
    name=models.CharField(max_length=50)
    ceo=models.CharField(max_length=50)
    location=models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse('company_detail',kwargs={'pk':self.pk})









from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Posts(models.Model):
    Title = (
        ('Food','Food'),
        ('Clothes','Clothes'),
    )
    Type_Food = (
        ('Veg','Veg'),
        ('NonVeg','Nonveg'),
        ('Both','Both'),
    )
    title = models.CharField(max_length=200,null=False,choices=Title)
    Phone = models.IntegerField(null=True)
    type_food = models.CharField(max_length=200,null=True,choices=Type_Food)
    pickup_location =models.CharField(max_length=200,null=True)
    food_fresh = models.FloatField(null=True)
    served_people = models.FloatField(null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

class organizations(models.Model):
    org_name = models.CharField(max_length=100)

    def __str__(self):
        return self.org_name
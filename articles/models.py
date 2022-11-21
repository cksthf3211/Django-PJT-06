from django.db import models
from django.conf import settings

# Create your models here.

class Article(models.Model):
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='articles', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="article/", blank=True)
    category = models.TextField()
    studio = models.TextField()


class Search(models.Model):
    keyword = models.TextField(max_length=30)
    count = models.IntegerField(default=1)



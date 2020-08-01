from django.db import models
from django.contrib.auth.models import AbstractUser
from news.models import NewsClass

class User(AbstractUser):
    name           = models.CharField(max_length=200,null=True)
    fav_news_class = models.ManyToManyField(NewsClass,blank=True,null=True)

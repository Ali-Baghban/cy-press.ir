from django.db import models

class About(models.Model):
    title       = models.CharField(max_length=200)
    paragraph_1 = models.TextField()
    paragraph_2 = models.TextField(default="")
    paragraph_3 = models.TextField(default="")
    paragraph_4 = models.TextField(default="")
    photo_main  = models.ImageField(upload_to='media/%Y/%m/%d/')
    def __str__(self):
        return self.title

class Contact(models.Model):
    comment = models.TextField()
    name    = models.CharField(max_length=200)
    email   = models.EmailField()
    def __str__(self):
        return self.name

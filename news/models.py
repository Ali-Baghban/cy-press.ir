from django.db import models

class NewsClass(models.Model):
    title       = models.CharField(max_length=100)
    def __str__(self):
        return self.title

class New(models.Model):
    title       = models.CharField(max_length=200,blank=False)
    body        = models.TextField(blank=False)
    news_class  = models.ManyToManyField('NewsClass')
    photo_main  = models.ImageField(upload_to='media/%Y/%m/%d/',blank=True)
    photo_more  = models.ImageField(upload_to='media/%Y/%m/%d/',blank=True)
    tags        = models.TextField(blank=True)
    published   = models.DateTimeField(auto_now=True)
    view_count  = models.IntegerField(editable=True,default=0,null=True)

    def __str__(self):
        return self.title

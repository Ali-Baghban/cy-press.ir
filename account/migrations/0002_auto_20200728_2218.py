# Generated by Django 3.0.7 on 2020-07-28 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_auto_20200727_2325'),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='fav_news_class',
            field=models.ManyToManyField(blank=True, null=True, to='news.NewsClass'),
        ),
    ]

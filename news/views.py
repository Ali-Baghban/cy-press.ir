from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate
from account.models import User
from .models import New, NewsClass


def index(request):
    if request.user.is_authenticated:
        user = get_object_or_404(User, username=request.user)
        news_cat = user.fav_news_class.all()
        footer_cat = NewsClass.objects.all()
        news_list = []
        for cat in news_cat:
            news = New.objects.filter(news_class=cat).order_by('-view_count')[:1]
            for n in news:
                n.category = cat.title
                news_list.append(n)
        for n in news_list:
            n.body = n.body[:100]
        latest_news = []
        for cat in news_cat:
            news = New.objects.filter(news_class=cat).order_by('-published')[:1]
            for n in news:
                n.category = cat.title
                latest_news.append(n)
        # Head news :
        head_news = New.objects.all().order_by('-view_count')[:1]
        for n in head_news:
            n.category = n.news_class.first()
        context = {
            'news_cat': news_cat, 'news_list': news_list, 'latest_news': latest_news,
            'head_news':head_news, 'footer_cat': footer_cat,
        }
        return render(request, 'pages/index.html', context=context)
    else:
        news_cat = NewsClass.objects.all()
        footer_cat = news_cat
        news_list = []
        for cat in news_cat:
            news = New.objects.filter(news_class=cat).order_by('-view_count')[:1]
            for n in news:
                n.category = cat.title
                news_list.append(n)
        for n in news_list:
            n.body = n.body[:100]
        latest_news = New.objects.order_by('-published')[:3]
        for n in latest_news:
            n.category = n.news_class.first().title
        # Head News :
        head_news = New.objects.all().order_by('-view_count')[:1]
        for n in head_news:
            n.category = n.news_class.first()
        context = {
            'news_cat': news_cat,
            'news_list': news_list,
            'latest_news': latest_news,
            'head_news':head_news,
            'footer_cat': footer_cat
        }
        return render(request, 'pages/index.html', context=context)


def news_category(request, category):
    footer_cat = NewsClass.objects.all()
    category = get_object_or_404(NewsClass, title=category)
    all_news = New.objects.all()
    news = all_news.filter(news_class=category).order_by('-view_count')
    latest_news = all_news.order_by('-published')[:5]
    for n in news:
        n.body = n.body[:100]
    context = {'news': news, 'category': category, 'latest_news': latest_news, 'footer_cat': footer_cat}
    return render(request, 'pages/category.html', context=context)


def news(request, category, news_id):
    category = get_object_or_404(NewsClass, title=category)
    footer_cat = NewsClass.objects.all()
    news = get_object_or_404(New, id=news_id, news_class=category)
    news.view_count = news.view_count + 1
    news.save()
    news.tags = news.tags.split(",")
    all_news = New.objects.filter(news_class=category)
    trending_news = all_news.order_by('-view_count')[:3]
    latest_news = all_news.order_by('-published')[:4]
    for n in trending_news:
        n.category = n.news_class.first()
    for n in latest_news:
        n.category = n.news_class.first()
    context = {'news': news, 'trending_news': trending_news, 'latest_news': latest_news, 'footer_cat': footer_cat}
    return render(request, 'pages/news.html', context=context)

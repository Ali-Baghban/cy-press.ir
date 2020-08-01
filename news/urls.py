from django.urls import path
from .views import index, news_category, news

urlpatterns = [
    path('', index, name='index'),
    path('<category>', news_category, name='category'),
    path('cat/<category>/<int:news_id>', news, name='news'),
]

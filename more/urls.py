from django.urls import path
from .views import about,contact

urlpatterns = [
    path('about', about, name='about'),
    path('contact', contact, name='contact'),

]
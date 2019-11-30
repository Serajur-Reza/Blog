from django.urls import path, include
from .views import post, show_post, search

urlpatterns = [
    path('', show_post),
    path('search/', search, name='search'),
    path('post/<pk>/',post, name='post_detail')
]
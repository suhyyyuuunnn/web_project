from django.urls import path
from .views import first, main, new


app_name = "posts"
urlpatterns = [
    path('first/', first, name="first"),
    path('main/', main, name="main"),
    path('new/', new, name="new"),
]

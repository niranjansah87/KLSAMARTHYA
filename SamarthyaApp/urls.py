from django.urls import path,include
from .views import Gallery,Index,Profile,about,codebuster,instantspeech,mathbuzz,wordblocks,jam,sodoku,primesuspect,tug,smashkarts,passthebomb


urlpatterns = [
    path('', Index,name="home"),
    path('gallery/',Gallery,name="Gallery"),
    path('user/<int:pk>/profile/',Profile,name="profile"),
    path('about',about,name="about"),
    path('codebuster',codebuster,name="codebuster"),
    path('mathbuzz',mathbuzz,name="mathbuzz"),
    path('wordblocks',wordblocks,name="wordblocks"),
    path('instantspeech',instantspeech,name="instantspeech"),
    path('jam',jam,name="jam"),
    path('sodoku',sodoku,name="sodoku"),
    path('primesuspect',primesuspect,name="primesuspect"),
    path('tug',tug,name="tug"),
    path('smashkarts',smashkarts,name="smashkarts"),
    path('passthebomb',passthebomb,name="passthebomb"),
]
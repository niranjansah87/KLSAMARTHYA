from django.urls import path,include
from .views import Gallery,Index,profile,about,codebuster,instant_speech,math_buzz,word_blocks,jam

urlpatterns = [
    path('', Index,name="home"),
    path('gallery/',Gallery,name="Gallery"),
        # '<int:pk>/
    path('<int:pk>/profile/',profile,name="profile"),
    path('about',about,name="about"),
    path('codebuster',codebuster,name="codebuster"),
    path('math_buzz',math_buzz,name="math_buzz"),
    path('word_blocks',word_blocks,name="word_blocks"),
    path('instant_speech',instant_speech,name="instant_speech"),
    path('jam',jam,name="jam"),
]
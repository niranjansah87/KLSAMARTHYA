from django.urls import path,include
from .views import Gallery,Index,profile,about

urlpatterns = [
    path('', Index,name="home"),
    path('gallery/',Gallery,name="Gallery"),
        # '<int:pk>/
    path('<int:pk>/profile/',profile,name="profile"),
    path('about',about,name="about"),
]
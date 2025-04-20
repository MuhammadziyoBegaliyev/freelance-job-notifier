from django.urls import path
from .views import HomePageView, AboutPageView , AddMePageView


urlpatterns = [
    path('', AddMePageView.as_view(), name='addme'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('',HomePageView.as_view(), name='home')
]
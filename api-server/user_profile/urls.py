from django.urls import path
from .views import UserProfileList

urlpatterns = [
    path('profiles/', UserProfileList.as_view(), name='profile-list'),
]
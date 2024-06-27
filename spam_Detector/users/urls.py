from django.urls import path
from . import views

app_name='users'

urlpatterns = [
    path('register/', views.UserCreateView.as_view(), name='user-register'),
    path('profile/<int:pk>/', views.UserDetailView.as_view(), name='profile'),
]
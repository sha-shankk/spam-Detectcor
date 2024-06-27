from django.urls import path
from spam import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('create/', views.SpamCreateView.as_view(), name='spam-create'),
    path('detail/<int:pk>/', views.SpamDetailView.as_view(), name='spam-detail'),
]
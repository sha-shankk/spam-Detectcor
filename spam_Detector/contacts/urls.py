from django.urls import path
from contacts.views import ContactCreateView, ContactDetailView


urlpatterns = [
    path('create/', ContactCreateView.as_view(), name='create'),
    path('<int:pk>/', ContactDetailView.as_view(), name='detail'),
]

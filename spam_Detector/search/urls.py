from django.urls import path
from search.views import UserCreateView, UserDetailView, SearchByNameView, SearchByPhoneNumberView

urlpatterns = [
    path('register/', UserCreateView.as_view(), name='user-register'),
    path('profile/<int:pk>/', UserDetailView.as_view(), name='user-profile'),
    path('search/name/', SearchByNameView.as_view(), name='search-by-name'),
    path('search/phone/', SearchByPhoneNumberView.as_view(), name='search-by-phone'),
]

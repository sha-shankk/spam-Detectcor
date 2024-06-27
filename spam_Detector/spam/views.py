from rest_framework import generics, permissions
from spam.models import Spam
from .serializers import SpamSerializer
from django.shortcuts import render

class SpamCreateView(generics.CreateAPIView):
    queryset = Spam.objects.all()
    serializer_class = SpamSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        instance, created = Spam.objects.get_or_create(phone_number=serializer.validated_data['phone_number'])
        if not created:
            instance.spam_count += 1
            instance.save()

class SpamDetailView(generics.RetrieveAPIView):
    queryset = Spam.objects.all()
    serializer_class = SpamSerializer

# Add these views
def home(request):
    return render(request, 'spam/homepage.html')

def about(request):
    return render(request, 'spam/about.html')
# spam/views.py

def homepage_view(request):
    return render(request, 'homepage.html')

from django.contrib.auth import get_user_model
from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Q
from users.serializers import UserSerializer
from rest_framework import generics
from users.models import User

User = get_user_model()

class SearchByNameView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request):
        query = request.query_params.get('name', '')
        queryset = User.objects.filter(
            Q(username__istartswith=query) | Q(username__icontains=query)
        ).order_by('username')
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

class SearchByPhoneNumberView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer
    
    def get_queryset(self):
        phone_number = self.request.query_params.get('phone_number', '')
        return User.objects.filter(phone_number=phone_number)
class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
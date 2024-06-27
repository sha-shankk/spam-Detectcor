from django.db import models
from django.contrib.auth.models import AbstractUser
# users/models.py

from django.db import models



class User(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    # Add more fields as needed
    # Example:
    # bio = models.TextField(blank=True)  # Optional bio for the user
    pass
from django.db import models

class Spam(models.Model):
    phone_number = models.CharField(max_length=15, unique=True)
    spam_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.phone_number

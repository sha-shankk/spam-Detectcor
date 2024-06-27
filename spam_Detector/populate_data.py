import random
from django.contrib.auth import get_user_model
from contacts.models import Contact
from spam.models import Spam

User = get_user_model()

def create_users(num_users=100):
    for i in range(num_users):
        User.objects.create_user(
            username=f'user{i}',
            phone_number=f'+100000000{i}',
            password='password'
        )

def create_contacts(num_contacts=500):
    users = User.objects.all()
    for i in range(num_contacts):
        Contact.objects.create(
            owner=random.choice(users),
            name=f'Contact{i}',
            phone_number=f'+200000000{i}'
        )

def create_spam(num_spam=50):
    for i in range(num_spam):
        Spam.objects.create(
            phone_number=f'+300000000{i}',
            spam_count=random.randint(1, 10)
        )

if __name__ == '__main__':
    create_users()
    create_contacts()
    create_spam()

# contacts/views.py

from django.views.generic import CreateView, DetailView
from contacts.models import Contact
from contacts.serializers import ContactSerializer

class ContactCreateView(CreateView):
    model = Contact  # Assuming Contact is your model
    fields = ['name', 'email', 'phone_number']  # Specify the fields you want to include in the form
   
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class ContactDetailView(DetailView):
    model = Contact
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

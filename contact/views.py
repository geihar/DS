from django.views.generic import CreateView

from .models import Contacts
from .forms import ContactsForm


class ContactView(CreateView):
    model = Contacts
    form_class = ContactsForm
    success_url = '/'


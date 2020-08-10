from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.generic import CreateView

from .models import Contacts
from .forms import ContactsForm


class ContactView(CreateView):
    model = Contacts
    form_class = ContactsForm
    success_url = '/'

    def post(self, request):
        form = ContactsForm(request.POST)
        if form.is_valid():
            Contacts.objects.update_or_create(
                email=request.POST.get("email")
            )
            return redirect('/')
        else:
            return redirect('/')


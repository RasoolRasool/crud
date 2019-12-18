from django.shortcuts import render
from .models import Contact
from django.views.generic import ListView,DeleteView,DetailView,CreateView,UpdateView
from django.urls import reverse_lazy
# Create your views here.

class ContactListview(ListView):
    model= Contact

class ContactDetailView(DetailView):
    model=Contact

class ContactUpdateView(UpdateView):
    model=Contact
    fields=['name','email']

class ContactCreateView(CreateView):
    model=Contact
    fields='__all__'

class ContactDeleteView(DeleteView):
    model=Contact
    success_url=reverse_lazy('contact_list')
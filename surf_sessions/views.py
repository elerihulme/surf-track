from django.shortcuts import render
from django.views import generic
from .models import Session

# Create your views here.
class SessionList(generic.ListView):
    queryset = Session.objects.all()
    template_name = "session_list.html"
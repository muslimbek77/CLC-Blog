from django.shortcuts import render
from rest_framework import generics
# Create your views here.
from contact.models import Cantact
from contact.serializers import ContactCreateSerializer
"""
TODO:
    - CreateAPIView 

"""

class CreateContactView(generics.CreateAPIView):
    queryset = Cantact.objects.all()
    serializer_class = ContactCreateSerializer
    


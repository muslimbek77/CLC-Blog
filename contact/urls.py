from django.urls import path, include
from contact.views import CreateContactView
urlpatterns = [
    path('contact/', CreateContactView.as_view()),
]

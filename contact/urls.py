# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.urls import path

from contact import views

# Urls for the contact page
urlpatterns = [
    path("contact/", views.ContactMessage.as_view(), name="contact"),
]

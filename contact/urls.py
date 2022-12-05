from . import views
from django.urls import path

urlpatterns = [
    path('', views.contact_details, name='contact_details'),
    path('edit_contact_details/', views.edit_contact_details, name='edit_contact_details'),
]
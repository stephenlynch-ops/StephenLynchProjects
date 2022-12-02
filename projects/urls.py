from . import views
from django.urls import path

urlpatterns = [
    path('<project_id>', views.project_detail, name='project_detail')
]
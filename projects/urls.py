from . import views
from django.urls import path

urlpatterns = [
    path('<project_id>', views.project_detail, name='project_detail'),
    path('add/', views.add_project, name='add_project'),
    path('edit/<int:project_id>', views.edit_project, name='edit_project'),
    path('delete/<int:project_id>', views.delete_project, name='delete_project'),
]
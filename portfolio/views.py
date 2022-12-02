from django.shortcuts import render, get_object_or_404
from django.views import generic
from projects.models import Project


class ProjectList(generic.ListView):
    model = Project
    queryset = Project.objects.filter(status=1).order_by('-post_date')
    template_name = 'index.html'
    paginate_by = 6

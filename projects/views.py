from django.shortcuts import render, get_object_or_404
from . models import Project


def project_detail(request, project_id):
    """ A view to show the selected project in more detail """

    project = get_object_or_404(Project, pk=project_id)

    context = {
        'project': project,
    }

    return render(request, 'project_detail.html', context)

from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from . models import Project
from . forms import ProjectForm


def project_detail(request, project_id):
    """ A view to show the selected project in more detail """

    project = get_object_or_404(Project, pk=project_id)

    context = {
        'project': project,
    }

    return render(request, 'project_detail.html', context)


def add_project(request):
    """ A view to add a project to the database """

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Project has successfully been added!')
            return redirect(('home'))
        else:
            messages.error(request, 'Project could not be added at this time, check the form is valid')
    else:
        form = ProjectForm()

    template = 'add_project.html'

    context = {
        'form': form
    }

    return render(request, template, context)


def edit_project(request, project_id):
    """ Edit a project in the database """
    project = get_object_or_404(Project, pk=project_id)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, f'Successfully updated {project.project_title}')
        else:
            messages.error(request, f'Unable to update {project.project_title}!')
    else:
        form = ProjectForm(instance=Project)
        messages.info(request, f'You are editing {project.project_title}')

    template = 'edit_project.html'
    context = {
        'form': form,
        'project': project,
    }

    return render(request, template, context)


def delete_project(request, project_id):
    """ A view to delete a project from the database """
    project = get_object_or_404(Project, pk=project_id)
    project.delete()
    messages.success(request, 'Project deleted!')
    return redirect(reverse('home'))

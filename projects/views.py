from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from . models import Project
from . forms import ProjectForm


def project_detail(request, project_id):
    """ A view to show the selected project in more detail """

    project = get_object_or_404(Project, pk=project_id)

    context = {
        'project': project,
    }

    return render(request, 'project_detail.html', context)


@login_required
def add_project(request):
    """ A view to add a project to the database """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry only Stephen can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save()
            messages.success(request, 'Successfully added project!')
            return redirect(reverse('project_detail', args=[project.id]))
        else:
            messages.error(request, 'Failed to add project. Please ensure the \
                form is valid.')
    else:
        form = ProjectForm()

    template = 'add_project.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_project(request, project_id):
    """ Edit a project in the database """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry only Stephen can do that.')
        return redirect(reverse('home'))

    project = get_object_or_404(Project, pk=project_id)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated project!')
            return redirect(reverse('project_detail', args=[project.id]))
        else:
            messages.error(request, 'Failed to update project. Please ensure \
                the form is valid.')
    else:
        form = ProjectForm(instance=project)
        messages.info(request, f'You are editing {project.project_title}')

    template = 'edit_project.html'
    context = {
        'form': form,
        'project': project,
    }

    return render(request, template, context)


@login_required
def delete_project(request, project_id):
    """ A view to delete a project from the database """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry only store owners can do that.')
        return redirect(reverse('home'))

    project = get_object_or_404(Project, pk=project_id)
    project.delete()
    messages.success(request, 'Project deleted!')
    return redirect(reverse('home'))

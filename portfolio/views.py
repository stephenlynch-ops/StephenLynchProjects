from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from projects.models import Project


def portfolio(request):
    """ A view to show all projects, including search queries """

    projects = Project.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria")
                return redirect(reverse('home'))

            queries = Q(language_summary__icontains=query)
            projects = projects.filter(queries).order_by('post_date')

    context = {
        'projects': projects,
        'search_term': query,
    }

    return render(request, 'index.html', context)

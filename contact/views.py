from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Contact
from .forms import ContactForm


def contact_details(request):
    """ A view to show the contact details page """

    contact = Contact.objects.get(id=1)
    template = 'contact_details.html'

    context = {
        'contact': contact,
    }

    return render(request, template, context)


@login_required
def edit_contact_details(request):
    """ Edit the contact details """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry only Stephen can do that.')
        return redirect(reverse('home'))

    contact = Contact.objects.get(id=1)
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES, instance=contact)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated contact details!')
            return redirect(reverse('contact_details'))
        else:
            messages.error(request, 'Failed to update contact details. Please check the form is valid.')
    else:
        form = ContactForm(instance=contact)
        messages.info(request, 'You are editing the contact details')

    template = 'edit_contact_details.html'
    context = {
        'form': form,
        'contact': contact,
    }

    return render(request, template, context)

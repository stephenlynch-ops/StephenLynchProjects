from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'linkedin',
        'github_repo',
        'about_me',
    )


admin.site.register(Contact, ContactAdmin)

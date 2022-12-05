from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'user_name',
        'user_image',
        'email',
        'linkedin',
        'github_repo',
        'about_me',
    )


admin.site.register(Contact, ContactAdmin)

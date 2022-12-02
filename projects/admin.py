from django.contrib import admin
from .models import Project
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Project)
class ProjectAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('project_title',)}
    list_filter = ('status', 'post_date')
    list_display = ('project_title', 'status', 'post_date', 'html', 'css',
                    'javascript', 'python', 'flask', 'react', 'django',
                    'bootstrap', 'java', 'sql', 'jquery')
    search_fields = ('project_title', 'task', 'actions', 'problems',
                     'knowledge_gained')
    summernote_fields = ('task', 'actions', 'problems',
                         'knowledge_gained')

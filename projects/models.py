from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = (
    (0, 'Draft'),
    (1, 'Published')
)


class Project(models.Model):
    project_title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    headline = models.CharField(max_length=200, null=True, blank=True)
    post_date = models.DateField(auto_now_add=True)
    task = models.TextField(null=True, blank=True)
    actions = models.TextField(null=True, blank=True)
    problems = models.TextField(null=True, blank=True)
    knowledge_gained = models.TextField(null=True, blank=True)
    image1 = CloudinaryField('image1', default='placeholder')
    image2 = CloudinaryField('image2', default='placeholder')
    image3 = CloudinaryField('image3', default='placeholder')
    html = models.BooleanField(default=False)
    css = models.BooleanField(default=False)
    javascript = models.BooleanField(default=False)
    python = models.BooleanField(default=False)
    flask = models.BooleanField(default=False)
    react = models.BooleanField(default=False)
    django = models.BooleanField(default=False)
    bootstrap = models.BooleanField(default=False)
    java = models.BooleanField(default=False)
    sql = models.BooleanField(default=False)
    jquery = models.BooleanField(default=False)
    status = models.IntegerField(choices=STATUS, default=0)


class Meta:
    ordering = ['-post_date']


def __str__(self):
    return self.project_title

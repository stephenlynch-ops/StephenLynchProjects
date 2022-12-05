from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Contact(models.Model):
    """ The contct detail for the user (me) """
    user_name = models.CharField(max_length=50, null=True, blank=True)
    user_image = CloudinaryField('user_image', default='noface', null=True, blank=True)
    email = models.EmailField(max_length=50, null=True, blank=True)
    linkedin = models.URLField(max_length=1054, null=True, blank=True)
    github_repo = models.URLField(max_length=1054, null=True, blank=True)
    facebook = models.URLField(max_length=1054, null=True, blank=True)
    twitter = models.URLField(max_length=1054, null=True, blank=True)
    about_me = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.email

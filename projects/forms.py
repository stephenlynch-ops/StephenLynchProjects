from .models import Project
from django import forms


class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = '__all__'

    image1 = forms.ImageField(label='Image1', required=False)
    image2 = forms.ImageField(label='Image2', required=False)
    image3 = forms.ImageField(label='Image3', required=False)

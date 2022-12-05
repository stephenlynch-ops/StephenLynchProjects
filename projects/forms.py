from .models import Project
from django import forms


class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = '__all__'

    image1 = forms.ImageField(label='Image 1', required=False)
    image2 = forms.ImageField(label='Image 2', required=False)
    image3 = forms.ImageField(label='Image 3', required=False)
    image4 = forms.ImageField(label='Image 4', required=False)
    image5 = forms.ImageField(label='Image 5', required=False)

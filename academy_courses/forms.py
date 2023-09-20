from django import forms
from .models import Course, Video


field_attrs = {'class': 'form-control'}

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'description', 'price', 'hour', 'min', 'image']
        widgets = {
            'name': forms.TextInput(attrs=field_attrs),
            'description': forms.Textarea(attrs=field_attrs),
        }


class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['title', 'desc', 'video', 'course']
        widgets = {
            'title': forms.TextInput(attrs=field_attrs),
            'desc': forms.Textarea(attrs=field_attrs),
            'course': forms.Select(attrs=field_attrs),
        }
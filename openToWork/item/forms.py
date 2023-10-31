from django import forms
from .models import Project

from .models import Item

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'


class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'description', 'is_open_for_part_time_work', 'image', 'video')
        widgets = {
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'is_open_for_part_time_work': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            }),
            'video': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            })  
        }

class EditProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('title', 'description', 'cover_image', 'demo_link', 'demo_video')
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'INPUT_CLASSES',  # Make sure to replace 'INPUT_CLASSES' with the actual CSS class you want to use
            }),
            'description': forms.Textarea(attrs={
                'class': 'INPUT_CLASSES',
            }),
            'cover_image': forms.FileInput(attrs={
                'class': 'INPUT_CLASSES',
            }),
            'demo_link': forms.URLInput(attrs={
                'class': 'INPUT_CLASSES',
            }),
            'demo_video': forms.FileInput(attrs={
                'class': 'INPUT_CLASSES',
            })
        }
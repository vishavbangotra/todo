from django import forms
from django.forms import ModelForm
from basicapp.models import *

class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = '__all__'
        widgets = {
            'title': forms.TextInput
                               (attrs={'placeholder':'New Task'}),
        }

from django import forms
from basicapp.models import Todo
class TaskForm(forms.ModelForm):
    title = forms.CharField(max_length=128, widget=forms.TextInput
                           (attrs={'placeholder':'Enter a task'}))
    class Meta:
        model = Todo
        fields = '__all__'

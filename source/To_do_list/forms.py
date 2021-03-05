from django import forms
from To_do_list.models import status_choices


class TaskForm(forms.form):
    title = forms.CharField(max_length=250, required=True)
    status = forms.ChoiceField(choices=status_choices, )
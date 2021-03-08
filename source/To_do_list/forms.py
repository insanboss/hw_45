from django import forms


from To_do_list.models import status_choices


class TaskForm(forms.Form):
    title = forms.CharField(max_length=250, required=True)
    status = forms.ChoiceField(choices=status_choices, required=False)
    date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    add_info = forms.CharField(max_length=300, required=False, widget=forms.Textarea)
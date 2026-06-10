from django import forms    

class ToDo(forms.Form):
    title = forms.CharField(label="Name of your newly added task", max_length=60)
    description = forms.CharField(label="The detailed description of your task")
    due_date = forms.DateTimeField(label="Due date",widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
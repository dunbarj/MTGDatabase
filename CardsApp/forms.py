from django import forms

class SimpleForm(forms.Form):
    term = forms.CharField(label='Term', max_length=100)
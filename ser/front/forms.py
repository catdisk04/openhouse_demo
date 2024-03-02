from django import forms

class Inp_form(forms.Form):
    name = forms.CharField(label="Enter your name")
    hash = forms.CharField(label="")

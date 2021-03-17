from django import forms

class RegistrationForm(forms.Form):
    username = forms.CharField(label="Username: ", max_length=255)
    password = forms.CharField(label="Password: ", max_length=255)

class RetrieveForm(forms.Form):
    username = forms.CharField(label="Username: ", max_length=255)
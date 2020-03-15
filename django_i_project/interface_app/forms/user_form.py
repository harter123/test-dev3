from django import forms


class UserForm(forms.Form):
    username = forms.CharField(max_length=50,
                               min_length=3,
                               required=True)
    password = forms.CharField(max_length=50,
                               min_length=3,
                               required=True)


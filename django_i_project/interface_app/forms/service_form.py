from django import forms


class ServiceForm(forms.Form):
    name = forms.CharField(max_length=200,
                           min_length=1,
                           required=True)
    description = forms.CharField(max_length=2000,
                                  min_length=1,
                                  required=True)

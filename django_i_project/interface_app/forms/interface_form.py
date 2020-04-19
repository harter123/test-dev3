from django import forms


class InterfaceForm(forms.Form):
    name = forms.CharField(max_length=200,
                           min_length=1,
                           required=True)
    description = forms.CharField(max_length=2000,
                                  min_length=1,
                                  required=True)
    service_id = forms.IntegerField(required=True)
    context = forms.CharField(max_length=5000,
                              min_length=1,
                              required=True)

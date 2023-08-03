# myapp/forms.py

# myapp/forms.py

from django import forms

class MyForm(forms.Form):
    # Define your form fields here
    field1 = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'custom-class', 'id': 'field1'})
    )
    field2 = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'custom-class', 'id': 'field2'})
    )
    # Add more fields as needed

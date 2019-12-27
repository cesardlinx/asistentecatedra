from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=20)
    email = forms.EmailField(max_length=50)
    subject = forms.CharField(max_length=20)
    message = forms.CharField(max_length=500, widget=forms.Textarea)


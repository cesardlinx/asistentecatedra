from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=20, label="Nombre")
    email = forms.EmailField(max_length=50, label="Email")
    subject = forms.CharField(max_length=20, label="Asunto")
    message = forms.CharField(max_length=500, label="Mensaje",
                              widget=forms.Textarea)

from django import forms
from Base_Application.models import ContactUs


# Writing Forms here

class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = "__all__"

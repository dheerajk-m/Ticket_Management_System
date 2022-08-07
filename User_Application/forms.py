from django import forms
from User_Application.models import UserRegistrationData, UserTicket


# writing forms here

class UserRegistrationDataForm(forms.ModelForm):
    class Meta:
        model = UserRegistrationData
        fields = "__all__"


class UserTicketForm(forms.ModelForm):
    class Meta:
        model = UserTicket
        fields = ["user", "title", "description"]

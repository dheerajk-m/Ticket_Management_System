from django.shortcuts import render
from Base_Application.models import ContactUs
from Base_Application.forms import ContactUsForm


# Create your views here.

def homepage(request):
    return render(request, "homepage.html", {})


def about_us(request):
    return render(request, "about_us.html", {})


def contact_us(request):
    # checking the request method
    if request.method == "POST":
        contact_info = ContactUsForm(request.POST)
        print("Contact_Form_Errors: ", contact_info.errors)
        # checking the validity of the obtained form data

        if contact_info.is_valid():
            # saving the data in the database
            contact_info.save()
            success_context = {"success_message": "Your message has been sent. Thank you for contacting us!"}
            return render(request, "contact_us.html", success_context)
        else:
            contact_info = ContactUsForm(request.POST)
            # passing error message if the form data isn't valid
            error_context = {"error_message": "Oops! An unexpected error occurred", "contact_info": contact_info}
            return render(request, "contact_us.html", error_context)

    return render(request, "contact_us.html", {})

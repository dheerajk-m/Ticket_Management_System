from django.shortcuts import render
from User_Application.models import UserRegistrationData, UserTicket
from User_Application.forms import UserRegistrationDataForm, UserTicketForm


# Create your views here.

# Creating User Login View
def login(request):
    if request.method == "POST":
        # requesting data from the user
        email = request.POST["email_id"]
        password = request.POST["password"]
        email_count = UserRegistrationData.objects.filter(email_id=email)
        user_count = UserRegistrationData.objects.filter(email_id=email, password=password)

        # Initiating Exception Handling
        try:
            # Checking whether a user is registered with the given Email
            if len(email_count) == 0:
                context = {"user_doesnt_exist": "An account with " + email + " doesn't Exist. Please Register!"}
                return render(request, "user_registration.html", context)
            # Checking whether the given email and password match
            elif len(user_count) == 0:
                context = {"invalid_credentials": "You have entered Invalid Credentials :("}
                return render(request, "user_login.html", context)
            else:
                # Creating a session and logging in, since the user exists with given details
                request.session["email"] = email
                user_data = UserRegistrationData.objects.get(email_id=email)
                context = {"login_success": "Welcome " + user_data.first_name}
                return render(request, "user_homepage.html", context)

        # Logging any exceptions that might have triggered
        except Exception as error:
            print("Login Error: ", error)
            context = {"error_message": "Uh oh! An unexpected error occurred!"}
            return render(request, "user_login.html", context)

    return render(request, "user_login.html", {})


# Creating User Registration View
def registration(request):
    if request.method == "POST":
        email = request.POST["email_id"]
        email_count = UserRegistrationData.objects.filter(email_id=email)
        try:
            user_form_data = UserRegistrationDataForm(request.POST)
            print("User Form Data Errors: ", user_form_data.errors)

            # Filtering Duplicate Email Registration
            if len(email_count) == 1:
                context = {"user_exists": "User with " + email +
                                          "already exists! Please register with another email :)"}
                return render(request, "user_registration.html", context)
            # Saving User Data in Database if there's no Duplicate
            elif user_form_data.is_valid():
                user_form_data.save()
                context = {"success": "Registration Successful! Login for full experience"}
                return render(request, "user_login.html", context)

        except Exception as error:
            print("Registration Error: ", error)
            context = {}
            return render(request, "user_registration.html", context)
    return render(request, "user_registration.html", {})


# Creating User logout View
def logout(request):
    del request.session["email"]
    return render(request, "user_login.html", {"success": "Logged Out Successfully :)"})


# Creating Session Validator
def is_login(request):
    if request.session.__contains__("email"):
        return True
    else:
        return False


# Creating User Homepage View
def homepage(request):
    if is_login(request):
        email = request.session["email"]
        user_data = UserRegistrationData.objects.get(email_id=email)
        context = {"login_success": "Welcome " + user_data.first_name}
        return render(request, "user_homepage.html", context)

    else:
        context = {"not_logged_in": "User not logged in :/ Please login to continue :D"}
        return render(request, "user_login.html", context)


# Creating a New Ticket View
def new_ticket(request):
    if is_login(request):
        email = request.session["email"]
        user_data = UserRegistrationData.objects.get(email_id=email)
        context = {"user": user_data}
        return render(request, "user_new_ticket.html", context)

    else:
        context = {"not_logged_in": "User not logged in :/ Please login to continue :D"}
        return render(request, "user_login.html", context)


# Saving the Ticket in the Database
def new_ticket_save(request):
    if is_login(request):
        if request.method == "POST":
            try:
                ticket_form_data = UserTicketForm(request.POST)
                print("Ticket Form Errors", ticket_form_data.errors)

                if ticket_form_data.is_valid():
                    ticket_form_data.save()

                    email = request.session["email"]
                    user_data = UserRegistrationData.objects.get(email_id=email)
                    ticket_data = UserTicket.objects.filter(user_id=user_data.id)

                    context = {"success": "Ticket Submission Successful :D", "ticket_data": ticket_data}
                    return render(request, "user_view_ticket.html", context)
                else:
                    context = {"error_message": "Uh oh! An unexpected error occurred ;-;"}
                    return render(request, "user_new_ticket.html", context)

            except Exception as error:
                print("Ticket Saving Error", error)
                context = {"error_message": "Uh oh! An unexpected error occurred ;-;"}
                return render(request, "user_new_ticket.html", context)
        return render(request, "user_new_ticket.html", {})

    else:
        context = {"not_logged_in": "User not logged in :/ Please login to continue :D"}
        return render(request, "user_login.html", context)


# Displaying Existing User Tickets
def view_tickets(request):
    if is_login(request):
        email = request.session["email"]
        user_data = UserRegistrationData.objects.get(email_id=email)
        ticket_data = UserTicket.objects.filter(user_id=user_data.id)
        context = {"ticket_data": ticket_data}
        return render(request, "user_view_ticket.html", context)
    else:
        context = {"not_logged_in": "User not logged in :/ Please login to continue :D"}
        return render(request, "user_login.html", context)


# Modifying Existing User Tickets
def edit_ticket(request, ticket_id):
    if is_login(request):
        ticket_data = UserTicket.objects.get(id=ticket_id)
        context = {"ticket_data": ticket_data}
        return render(request, "user_edit_ticket.html", context)
    else:
        context = {"not_logged_in": "User not logged in :/ Please login to continue :D"}
        return render(request, "user_login.html", context)


# Saving the Ticket Modification in the Database
def update_user_ticket(request):
    if is_login(request):
        if request.method == "POST":
            try:
                ticket_id = request.POST["id"]
                ticket_instance = UserTicket.objects.get(id=ticket_id)
                ticket_form_data = UserTicketForm(request.POST, instance=ticket_instance)
                print("Ticket Form Errors", ticket_form_data.errors)
                if ticket_form_data.is_valid():
                    ticket_form_data.save()

                    email = request.session["email"]
                    user_data = UserRegistrationData.objects.get(email_id=email)
                    ticket_data = UserTicket.objects.filter(user_id=user_data.id)

                    context = {"success": "Ticket Edited Successfully :D", "ticket_data": ticket_data}
                    return render(request, "user_view_ticket.html", context)
                else:
                    context = {"error_message": "Uh oh! An unexpected error occurred ;-;"}
                    return render(request, "user_new_ticket.html", context)

            except Exception as error:
                print("Ticket Saving Error", error)
                context = {"error_message": "Uh oh! An unexpected error occurred ;-;"}
                return render(request, "user_new_ticket.html", context)
        return render(request, "user_new_ticket.html", {})

    else:
        context = {"not_logged_in": "User not logged in :/ Please login to continue :D"}
        return render(request, "user_login.html", context)

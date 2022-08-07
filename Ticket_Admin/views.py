from django.shortcuts import render
from User_Application.models import UserTicket, UserRegistrationData
from User_Application.forms import UserTicketForm, UserRegistrationDataForm


# Create your views here.

def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        if username == "Admin" and password == "TicketAdmin@123":
            request.session["username"] = username
            context = {"login_success": "Welcome Ticket Admin"}
            return render(request, "admin_homepage.html", context)
        else:
            context = {"invalid_credentials": "You have entered Invalid Credentials :("}
            return render(request, "admin_login.html", context)
    return render(request, "admin_login.html", {})


def logout(request):
    del request.session["username"]
    return render(request, "admin_login.html", {"success": "Logged Out Successfully :)"})


def is_login(request):
    if request.session.__contains__("username"):
        return True
    else:
        return False


def homepage(request):
    if is_login(request):
        context = {"login_success": "Welcome Ticket Admin"}
        return render(request, "admin_homepage.html", context)
    else:
        context = {"not_logged_in": "Admin not logged in :/ Please login to continue :D"}
        return render(request, "admin_login.html", context)


def view_all_tickets(request):
    if is_login(request):
        ticket_data = UserTicket.objects.all()
        context = {"ticket_data": ticket_data}
        return render(request, "admin_view_all_tickets.html", context)
    else:
        context = {"not_logged_in": "Admin not logged in :/ Please login to continue :D"}
        return render(request, "admin_login.html", context)


def edit_ticket_status(request, ticket_id):
    if is_login(request):
        ticket_data = UserTicket.objects.get(id=ticket_id)
        context = {"ticket_data": ticket_data}
        return render(request, "admin_edit_ticket-status.html", context)
    else:
        context = {"not_logged_in": "Admin not logged in :/ Please login to continue :D"}
        return render(request, "admin_login.html", context)


def update_ticket_status(request):
    if is_login(request):
        ticket_id = request.POST["id"]
        status = request.POST["status"]

        ticket_status = UserTicket.objects.get(id=ticket_id)
        ticket_status.status = status
        ticket_status.save()

        ticket_data = UserTicket.objects.all()
        context = {"ticket_data": ticket_data, "success": "Ticket Status Updated Successfully :D"}
        return render(request, "admin_view_all_tickets.html", context)

    else:
        context = {"not_logged_in": "Admin not logged in :/ Please login to continue :D"}
        return render(request, "admin_login.html", context)

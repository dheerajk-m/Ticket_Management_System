from django.urls import path
from User_Application import views as user_views

app_name = "User_Application"

urlpatterns = [
    path("", user_views.login, name="login"),
    path("registration", user_views.registration, name="registration"),
    path("logout", user_views.logout, name="logout"),
    path("home", user_views.homepage, name="homepage"),
    path("new_ticket", user_views.new_ticket, name="newTicket"),
    path("new_ticket_submission", user_views.new_ticket_save, name="newTicketSubmission"),
    path("view_my_tickets", user_views.view_tickets, name="viewTickets"),
    path("edit_my_ticket/<int:ticket_id>", user_views.edit_ticket, name="editUserTicket"),
    path("edit_my_ticket", user_views.update_user_ticket, name="UpdateUserTicket"),
]

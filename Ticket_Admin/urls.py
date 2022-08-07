from django.urls import path
from Ticket_Admin import views as admin_views

app_name = "Ticket_Admin"

urlpatterns = [
    path("", admin_views.login, name="login"),
    path("logout", admin_views.logout, name="logout"),
    path("home", admin_views.homepage, name="homepage"),
    path("view_user_tickets", admin_views.view_all_tickets, name="viewTickets"),
    path("edit_ticket-status/<int:ticket_id>", admin_views.edit_ticket_status, name="editTicketStatus"),
    path("update_ticket-status", admin_views.update_ticket_status, name="updateTicketStatus"),
]
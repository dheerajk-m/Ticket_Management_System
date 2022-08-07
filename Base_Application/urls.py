from django.urls import path
from Base_Application import views as base_views

app_name = "Base_Application"

urlpatterns = [
    path("", base_views.homepage, name="homepage"),
    path("about_us", base_views.about_us, name="about_us"),
    path("contact_us", base_views.contact_us, name="contact_us"),
]

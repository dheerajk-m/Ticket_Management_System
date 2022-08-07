from django.db import models
import datetime


# Create your models here.

class UserRegistrationData(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_id = models.EmailField()
    contact_number = models.BigIntegerField()
    password = models.CharField(max_length=50)

    objects = models.Manager()

    def __str__(self):
        return "%s" % self.first_name


class UserTicket(models.Model):
    user = models.ForeignKey(UserRegistrationData, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    create_on = models.DateTimeField(default=datetime.datetime.now, null=True)
    status = models.CharField(max_length=100, default="Under Review", null=True)

    objects = models.Manager()

    def __str__(self):
        return "%s" % self.title

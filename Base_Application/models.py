from django.db import models


# Create your models here.

class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email_ID = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    objects = models.Manager()

    def __str__(self):
        return "%s" % self.subject

from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20, null=False)
    email = models.CharField(max_length=50, null=False)
    password = models.CharField(max_length=100, null=False)

    def __str__(self):
        return f"{self.username} : {self.email}"
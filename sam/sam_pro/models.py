from django.db import models

# Create your models here.
class Login(models.Model):
    username = models.CharField(max_length=20, blank=False)
    email = models.EmailField()
    password = models.CharField(max_length=20,blank=False)
    mobile = models.CharField(max_length=10)

    def __str__(self):
        return self.username
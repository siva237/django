from django.db import models


# Create your models here.


# class RegistrationForm(models.Model):
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     password = models.CharField(max_length=10)
#
#     def __str__(self):
#         return self.first_name


class Marks(models.Model):
    rollno = models.CharField(max_length=10)
    telugu = models.IntegerField()
    english = models.IntegerField()
    maths = models.IntegerField()

    def __str__(self):
        return self.rollno


class Registration(models.Model):

    name = models.CharField(max_length=30)
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.name

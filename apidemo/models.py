from django.db import models


class Department(models.Model):
    title = models.CharField(max_length=100)


class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    department = models.ForeignKey(Department)
    birthdate = models.DateField(null=True, blank=True)

from django.db import models

class SalePerson(models.Model):
    # Define your fields here
    name = models.CharField(max_length=100)
    # Other fields can be added as needed

    def __str__(self):
        return self.name

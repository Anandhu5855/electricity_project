from django.db import models

class ElectricityStatus(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    has_electricity = models.BooleanField()

    def __str__(self):
        return self.name
from django.db import models

# Create your models here.
class Finch(models.Model):
    breed = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    length = models.IntegerField()
    region = models.CharField(max_length=100)

    def __str__(self):
        return self.name
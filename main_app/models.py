from django.db import models

# Create your models here.
class Record(models.Model):
    artist = models.CharField(max_length=100)
    album = models.CharField(max_length=100)
    released = models.IntegerField()

    def __str__(self):
        return self.album
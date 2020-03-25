from django.db import models
from django.urls import reverse

MEDIUM = (
    ('D', 'Digital'),
    ('C', 'Compact Disc'),
    ('V', 'Vinyl'),
)

class Distributor(models.Model):
    name = models.CharField(max_length=50)
    website = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('distributors_detail', kwargs={'pk': self.id})

# Create your models here.
class Record(models.Model):
    artist = models.CharField(max_length=100)
    album = models.CharField(max_length=100)
    released = models.IntegerField()
    distributors = models.ManyToManyField(Distributor)

    def __str__(self):
        return f"{self.artist}: {self.album}"
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'record_id': self.id})

class Listening(models.Model):
    date = models.DateField('Last listen')
    medium = models.CharField(
        max_length=1,
        choices=MEDIUM,
        default=MEDIUM[0][0]
        )

    record = models.ForeignKey(Record, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_medium_display()} on {self.date}"

    class Meta:
        ordering = ['-date']
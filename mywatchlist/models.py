from django.db import models

class MyWatchListItem(models.Model):
    watched = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    release_date = models.DateField()
    rating = models.IntegerField()
    review = models.TextField()

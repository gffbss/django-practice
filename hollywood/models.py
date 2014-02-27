from django.db import models

# Create your models here.

class Movie(models.Model):
    name = models.CharField(max_length=100)
    release_year = models.PositiveSmallIntegerField()

    def __unicode__(self):
        return self.name

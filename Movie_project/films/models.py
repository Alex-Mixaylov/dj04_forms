from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    poster = models.ImageField(upload_to='posters/', blank=True, null=True)
    description = models.TextField()
    release_date = models.DateField()
    review = models.TextField()

    def __str__(self):
        return self.title

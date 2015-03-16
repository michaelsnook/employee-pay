from django.db import models

# Create your models here.

class Giflink(models.Model):
    db_table = 'giflink';

    href = models.CharField("URL of the GIF", max_length=200, unique=True )
    title = models.CharField("GIF title", max_length=200, blank=True )
    category = models.SlugField(blank=True)

    def __str__(self):
        return self.title if self.title else self.href

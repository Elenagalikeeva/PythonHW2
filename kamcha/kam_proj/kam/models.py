from django.db import models


class Kam(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='kam/image/')
    url = models.URLField(blank=True)



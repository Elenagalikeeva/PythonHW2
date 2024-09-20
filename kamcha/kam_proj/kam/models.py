from django.db import models


class Kam(models.Model):
    title = models.CharField(max_length=300)
    description = models.CharField(max_length=300)
    image = models.ImageField(upload_to='kam/image/')
    url = models.URLField(blank=True)


    def __str__(self):
        return self.title


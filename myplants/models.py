from django.db import models
from django.conf import settings

class Plant(models.Model):
    name = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


    def __str__(self):
        return self.name


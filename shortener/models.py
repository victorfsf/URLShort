from django.db import models


class URLBase(models.Model):
    
    link = models.URLField()
    
    def __str__(self):
        return self.link
        
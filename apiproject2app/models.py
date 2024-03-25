from django.db import models

class Sample(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=100)
    last_updated_on = models.DateTimeField()
    is_active = models.BooleanField()
    created = models.DateTimeField()  

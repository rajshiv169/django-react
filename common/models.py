from django.db import models

# Create your models here.
class common(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    message = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
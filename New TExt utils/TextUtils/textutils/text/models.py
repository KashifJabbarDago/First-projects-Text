from django.db import models

# Create your models here.
class ContactUs(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    phone = models.CharField(max_length=150)
    msg = models.TextField()
    
    def __str__(self):
        return self.name 

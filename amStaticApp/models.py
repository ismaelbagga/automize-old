from django.db import models

# Create your models here.
class Contact(models.Model):
    name    = models.CharField(max_length = 50)
    email    = models.EmailField()
    Company = models.CharField(max_length = 100)
    Message = models.TextField()
    chik    = models.BooleanField(default = True)
    
    def __str__(self):
        return f'Message from {self.name}'




class Subscribe(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return f'Message from {self.email}'
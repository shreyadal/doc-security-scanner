from django.db import models

class Upload_document(models.Model):
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class user(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)

    
# Create your models here.

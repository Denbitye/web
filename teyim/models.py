from django.db import models




# Create your models here.
class Document(models.Model):
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=50, blank=True)
    description = models.TextField(max_length=300, blank=True)
    document = models.FileField(upload_to='documents/%Y/%m/%d/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class Contact(models.Model):
    id=models.AutoField(primary_key=True)
    fname=models.CharField(max_length=255)
    lname=models.CharField(max_length=255)
    email=models.EmailField()
    subject=models.CharField(max_length=255)
    message=models.TextField()
    def __str__(self):
        return self.fname 

class Images(models.Model):
    alt = models.CharField(max_length=60)
    image = models.ImageField(upload_to='img/%Y/%m/%d/', blank=True)


    def __str__(self):
        return self.alt
from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100,null=True)
    email = models.EmailField(max_length=100,null=True)
    subject = models.CharField(max_length=255,null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    class meta:
        db_table = "contact"
        

class Register(models.Model):
    name = models.CharField(max_length=100,null=True)
    email = models.EmailField(max_length=200,null=True)
    phone = models.CharField(max_length=50,null=True)
    program = models.CharField(max_length=100,null=True)
    notes = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    
    class meta:
        db_table = "student_register"
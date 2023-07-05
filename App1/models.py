from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.
class Camera_show(models.Model):
    Camera_Image=CloudinaryField('image')
    Camera_About=models.CharField(max_length=50)


    def __str__(self):
     return self.Camera_About


class Contact_form(models.Model):
   Name=models.CharField( max_length=80)
   Email=models.EmailField( max_length=180)
   Subject=models.CharField( max_length=180)
   Masg=models.CharField( max_length=2000)

   def __str__(self):
     return self.Name




class Signup_Form(models.Model):
   Name=models.CharField(max_length=50)
   Email=models.EmailField(max_length=50)
   Password=models.IntegerField()

   def __str__(self):
     return self.Name

   
class Suggestions_form(models.Model):
   Name=models.CharField(max_length=50)
   Phone=models.BigIntegerField()
   Email=models.EmailField(max_length=50)
   Topic=models.CharField(max_length=60)
   Misg=models.TextField(max_length=2000)


   def __str__(self):
     return self.Topic




from django.db import models

# Create your models here.

class Teacher(models.Model): #parent table
    firstname = models.CharField (max_length=50)
    Lastname = models.CharField (max_length=50)
    Email = models.EmailField (max_length=50)
    
    def __str__(self):
        return self.firstname

class student(models.Model): #child table
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE)
    firstname = models.CharField (max_length=50)
    Lastname = models.CharField (max_length=50)
    Email = models.EmailField (max_length=50)
    
    def __str__(self):
        return self.firstname
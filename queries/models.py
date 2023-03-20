from django.db import models
# Create your models here.

class Teacher(models.Model):  
    username = models.CharField(max_length=20)  
    firstname = models.CharField(max_length=30)  
    lastname = models.CharField(max_length=30)  
    mobile = models.CharField(max_length=10)  
    email = models.EmailField()  
  
    def __str__(self):  
        return "%s %s" % (self.firstname, self.lastname)  


class Employee(models.Model):
    emp_id = models.CharField(max_length=10)
    emp_fname = models.CharField(max_length=10)
    emp_lname = models.CharField(max_length=13)
    emp_dept = models.CharField(max_length=20)
    emp_city = models.CharField(max_length=20)

    def __str__(self):
        return "%s %s" % (self.emp_fname, self.emp_lname)
from django.db import models

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    


class Employee(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True, max_length=100)
    dept  = models.ForeignKey(Department, on_delete=models.CASCADE)
    salary = models.PositiveIntegerField()
    join_date = models.DateTimeField(auto_now_add=True)
    image     = models.ImageField(upload_to='Employee/images')
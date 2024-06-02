from django.db import models

# Create your models here.
class Emp(models.Model):
    name=models.CharField(max_length=200)
    emp_id=models.CharField(max_length=200)
    phone=models.CharField(max_length=10)
    address=models.CharField(max_length=150)
    working=models.BooleanField(default=True)
    department=models.CharField(max_length=10)


class Emp123(models.Model):
    email=models.EmailField(max_length=200)
    name=models.CharField(max_length=200)
    feedback=models.CharField(max_length=200)
    
        



class Testimonial(models.Model):
    name=models.CharField(max_length=200)
    testimonial=models.TextField()
    picture=models.ImageField(upload_to='Testimonial/')
    rating=models.IntegerField()

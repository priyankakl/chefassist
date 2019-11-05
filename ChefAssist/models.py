from django.db import models

# Create your models here.

class Recipe(models.Model):
    title=models.CharField(max_length=100)
    ingredients=models.CharField(max_length=400)
    instructions=models.CharField(max_length=500)
    notes=models.CharField(max_length=400)
    #added_on=models.DateField(blank=True, auto_now=True)
    total_time=models.IntegerField(null=True)
    
    def __str__(self):
        return self.title 

class Events(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255,null=True,blank=True)
    start = models.DateTimeField(null=True,blank=True)
    end = models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return self.name
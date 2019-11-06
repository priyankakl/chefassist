from django.db import models

# Create your models here.

class Recipe(models.Model):
    title=models.CharField(max_length=100)
    ingredients=models.CharField(max_length=800)
    instructions=models.CharField(max_length=800)
    notes=models.CharField(max_length=800)
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
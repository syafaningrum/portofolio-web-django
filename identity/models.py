from django.db import models


class Identity(models.Model):
    name       = models.CharField(max_length=120)
    email      = models.EmailField()
    instagram  = models.CharField(max_length=120, blank=True)
    linkdin    = models.CharField(max_length=120, blank=True)
    github     = models.CharField(max_length=120, blank=True)
    born_date  = models.DateField(auto_now_add=False)
    born_place = models.CharField(max_length=120, blank=True)
    timestamp  = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
        
class Education(models.Model):
    institution  = models.CharField(max_length=120)
    start        = models.CharField(max_length=120)
    end          = models.CharField(max_length=120)
    major        = models.CharField(max_length=120)
    def __str__(self):
        return self.institution
        
class Project(models.Model):
    name         = models.CharField(max_length=120)
    category     = models.CharField(max_length=120)
    purpose      = models.CharField(max_length=120)
    skill        = models.TextField(blank=True, null=True)
    description  = models.TextField(blank=True, null=True)
    date         = models.CharField(max_length=120)
    def __str__(self):
        return self.name

class Experience(models.Model):
    name       = models.CharField(max_length=120)
    category   = models.CharField(max_length=120)
    heldby     = models.CharField(max_length=120)
    date       = models.CharField(max_length=120)
    place      = models.CharField(max_length=120, blank=True)
    description= models.TextField(blank=True, null=True)
    def __str__(self):
        return self.name

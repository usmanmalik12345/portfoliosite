from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class Projects_Done(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    project_image = models.ImageField(upload_to='images_of_projects/', default = 'images_of_projects/default.jpg')
    links = models.CharField(max_length=500)
    def __str__(self):
        return self.title



class skills(models.Model):
    skill_name = models.CharField(max_length=100)
    percentage = models.IntegerField()
    def __str__(self):
        return self.skill_name


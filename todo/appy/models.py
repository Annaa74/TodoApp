from django.db import models

class Todo(models.Model):
    task = models.TextField()
    priority = models.CharField(max_length=10,default='low',)
    is_completed = models.BooleanField()
class Profile(models.Model):
    title = models.CharField(max_length=30)
    profile_pic = models.ImageField(upload_to="profile_pic/")
    
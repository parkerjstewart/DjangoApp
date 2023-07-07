from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

'''
models.py is where you define your data models in Django. 
Data models represent the structure and behavior of the data in your Django application.
It is typical to keep the models.py file within the directory of the app the models are used for

Data models are represented by Python classes that inherit from django.db.models.Model
'''

class Post(models.Model):
    title = models.CharField(max_length=140)
    content = models.TextField()
    # sets date posted to the current date/time only when the object was originally created
    # date_posted = models.DateTimeField(auto_now_add=True)
    date_posted = models.DateField(default=timezone.now)
    # every time the post is updated, the last_modified is updated with auto_now=True
    last_modified = models.DateField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.title

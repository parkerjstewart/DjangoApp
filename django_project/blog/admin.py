from django.contrib import admin
from .models import Post

# Register your models here.

'''
This is where you put the models that you want in the admin page
to register the post do:
'''

admin.site.register(Post)
from django.contrib import admin
from .models import Post

# make the model visible to the admin
admin.site.register(Post)
from django.contrib import admin

# Register your models here.
from .models import Post, Bien


admin.site.register(Post)
admin.site.register(Bien)
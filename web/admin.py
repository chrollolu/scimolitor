from django.contrib import admin

# Register your models here.
from .models import Post, Bien, Employe, Gallery, Client


admin.site.register(Post)
admin.site.register(Bien)
admin.site.register(Employe)
admin.site.register(Gallery)
admin.site.register(Client)
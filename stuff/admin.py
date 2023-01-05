from django.contrib import admin
from stuff.models import Stuff, Comment, Category

# Register your models here.

admin.site.register(Stuff)
admin.site.register(Comment)
admin.site.register(Category)
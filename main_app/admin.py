from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import About, GalleryImage

admin.site.register(About)
admin.site.register(GalleryImage)

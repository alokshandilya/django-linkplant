from django.contrib import admin

from .models import Link, Profile

# Register your models here.
admin.site.register(Profile)
admin.site.register(Link)

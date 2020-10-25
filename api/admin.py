from django.contrib import admin

# Register your models here.
from .models import Hero, yourMom
admin.site.register(Hero)
admin.site.register(yourMom)
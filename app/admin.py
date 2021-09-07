from django.contrib import admin

# Register your models here.
from . import models



@admin.register(models.People)
class PeopleAdmin(admin.ModelAdmin):
    pass

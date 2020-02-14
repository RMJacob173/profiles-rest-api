from django.contrib import admin

# Register your models here.
from profiles_app import models

admin.site.register(models.UserProfile)

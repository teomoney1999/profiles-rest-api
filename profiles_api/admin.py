from django.contrib import admin

from profiles_api import models

# Register your models here.

# Tell the Django register our user profile model with the Admin site
# Access from Admin site
admin.site.register(models.UserProfile)    
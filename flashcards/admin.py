from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
# add models to above import^^

# Register your models here.



admin.site.register(User, UserAdmin)

# admin.site.register(model)
# admin.site.register(model)

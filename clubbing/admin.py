from django.contrib import admin
from clubbing import models
from django.contrib.auth.admin import UserAdmin

admin.site.register(models.Item)
admin.site.register(models.Order)
admin.site.register(models.Purchase)
admin.site.register(models.User)
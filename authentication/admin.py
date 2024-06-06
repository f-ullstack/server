from django.contrib import admin
from .models import User, Profile, Product


class userProfile(admin.ModelAdmin):
    lst_display = ['fullName', 'email']

admin.site.register(Profile, userProfile)
admin.site.register(Product)
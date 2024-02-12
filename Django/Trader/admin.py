from django.contrib import admin
from .models import Record, UserProfile

# Register your models here.
admin.site.register(Record)
admin.site.register(UserProfile)
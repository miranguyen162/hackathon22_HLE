from django.contrib import admin
from class_app.models import *
from room.models import *

# Register your models here.

admin.site.register(Room)
admin.site.register(Message)
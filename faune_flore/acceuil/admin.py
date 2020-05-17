from django.contrib import admin
from .models import User
from .models import Species


admin.site.register(Species)
admin.site.register(User)

# Register your models here.

from django.contrib import admin
from .models import User
from .models import Plante


admin.site.register(Plante)
admin.site.register(User)

# Register your models here.

from django.contrib import admin
from .models import User
from .models import Molecule


admin.site.register(User)
admin.site.register(Molecule)

# Register your models here.

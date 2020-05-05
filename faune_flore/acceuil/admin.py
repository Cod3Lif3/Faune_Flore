from django.contrib import admin
from .models import Sujet	
from .models import Alimentation
from .models import User
from .models import Plante

admin.site.register(Sujet)
admin.site.register(Plante)
admin.site.register(Alimentation)
admin.site.register(User)

# Register your models here.

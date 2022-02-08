from django.contrib import admin
from . models import Robin
from . models import Place
# Register your models here.
admin.site.register(Place)
admin.site.register(Robin)
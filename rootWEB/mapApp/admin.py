from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(WwgUser)
admin.site.register(WwgVegan)
admin.site.register(WwgZerowaste)
admin.site.register(WwgClick)

admin.site.register(WwgZerowasteClick)
admin.site.register(WwgVeganClick)
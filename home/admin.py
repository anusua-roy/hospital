from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Room)
admin.site.register(Bed)
admin.site.register(Department)
admin.site.register(Doctor)
admin.site.register(Laboratory)
admin.site.register(Patient)
admin.site.register(Report)
admin.site.register(Admin)
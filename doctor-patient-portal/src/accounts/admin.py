from django.contrib import admin
from .models import User,UserTypes,Patient,Doctor


admin.site.register(UserTypes)
admin.site.register(User)
admin.site.register(Patient)
admin.site.register(Doctor)

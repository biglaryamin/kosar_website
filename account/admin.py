from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

UserAdmin.fieldsets += (
    ("فیلدهای ویژه",{"fields":('is_author','special_user','degree','job_position')}),
)

UserAdmin.list_display+=('is_author','is_special_user')
admin.site.register(User, UserAdmin)
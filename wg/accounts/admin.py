from django.contrib import admin
from wg.accounts.models import User

# Register your models here.

from rest_framework.authtoken.models import Token

# admin.site.register(Token)

class UserAdmin(admin.ModelAdmin):
    exclude = ('groups', 'user_permissions')


admin.site.register(User, UserAdmin)

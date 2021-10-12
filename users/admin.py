from django.contrib import admin
from django.utils.decorators import classonlymethod
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

import users
from .models import Profile
from users import models

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    list_display = ('pk','user','phone_number','website')
    list_display_links = ('pk','user')
    list_editable = ('phone_number','website')
    search_fields = ('user__first_name','user__email')
    list_filter=('created','modifird')

    fieldsets = (
        ('Profile',{
            'fields':(('user','phone_number'),),
        }),
        ('Extra info',{
            'fields':('website','biography')
        }   
        )
    )

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete= False
    verbose_name_plural = 'profiles'


class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)



admin.site.unregister(User)
admin.site.register(User , UserAdmin)
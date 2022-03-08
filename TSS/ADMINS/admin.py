from django.contrib import admin
from django.contrib.auth.admin import GroupAdmin,UserAdmin
from ADMINS.models import Profile, Tallent, UserDetails, Media, Follower,Role
from django.contrib.auth.models import Group,Permission
from django.utils.translation import gettext_lazy as _

# Register your models here.
class MyUserAdmin(UserAdmin):
 
    fieldsets = (
        (None, {'fields': ('username','password')}),
        (_('Personal info'), {'fields': ('first_name','last_name','email')}),
        (_('Permissions'), {'fields': ('is_active','is_superuser','groups','user_permissions')}),
        (_('Important dates'), {'fields': ('last_login','date_joined')}),
    )
    filter_vertical = ("user_permissions",)

    list_display = ("username","first_name","last_name","email","is_active")
    list_per_page = 15

class MediaAdmin(admin.ModelAdmin):
    list_display =("user","title","video_file","thumbnail","date_created","un_deleted")
    search_fields = ('title',)
    list_per_page = 15

class TallentAdmin(admin.ModelAdmin):
    list_display =("name","date_created","un_deleted")
    search_fields = ('name',)
    list_per_page = 15

class UserInfoAdmin(admin.ModelAdmin):
    list_display =("user","Tallent","artist_name","sex","phone","region","office_name","date_added","un_deleted")
    search_fields = ('user__username',)
    list_per_page = 15

class PermissionAdmin(admin.ModelAdmin):
    list_display =("name","codename")
    list_per_page = 15

class ProfileAdmin(admin.ModelAdmin):
    list_display =("user","image","date_updated")
    search_fields = ('user__username',)
    list_per_page = 15

class FollowerAdmin(admin.ModelAdmin):
    list_display =("user","phone","status","follow_date","un_deleted")
    search_fields = ('Media__title',)
    list_per_page = 15

admin.site.unregister(Group)
admin.site.register(Role, GroupAdmin)

admin.site.register(Permission,PermissionAdmin)
admin.site.register(Profile,ProfileAdmin)
admin.site.register(Tallent,TallentAdmin)
admin.site.register(UserDetails,UserInfoAdmin)
admin.site.register(Media,MediaAdmin)
admin.site.register(Follower,FollowerAdmin)

admin.site.site_url = "/home_url"

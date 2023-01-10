from django.contrib import admin
from .models import UserInfo

class UserInfoAdmin(admin.ModelAdmin):
    
    list_display = (
        'url',
        'avatar_url',
        'name',
        'full_name',
        'bio',
        'tags',
        'phone',
        'link',
        'posts',
        'count_followers',
        'followers',
        'count_following',
        'folowing',
        'user_id'
        )
    
    list_filter = (
        'posts',
        'count_followers',
        'count_following'   
        )
    
    search_fields = (
        'name',
        'full_name',
        'posts',
        'count_followers',
        'count_following'    
        )
    
admin.site.register(UserInfo, UserInfoAdmin)
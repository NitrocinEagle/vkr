from django.contrib import admin
from vkr.models import theory
from django.contrib.auth.models import Group
from loginsys.models import UserProfile


# Register your models here.

class theoryAdmin(admin.ModelAdmin):
    list_filter = ['theory_date']
    list_display = ['theory_title', 'theory_date']


class usersAdmin(admin.ModelAdmin):
    list_filter = ['study_group']
    list_display = ['last_name', 'first_name', 'study_group', ]
    fieldsets = (
        ('Персональные данные', {'fields': ('first_name', 'last_name', 'study_group',)}),
    )
    search_fields = ('last_name',)
    filter_horizontal = ()


admin.site.register(theory, theoryAdmin)
admin.site.register(UserProfile, usersAdmin)
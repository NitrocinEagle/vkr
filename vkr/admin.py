from django.contrib import admin
from vkr.models import theory


# Register your models here.

class theoryAdmin(admin.ModelAdmin):
    list_filter = ['theory_date']
    list_display = ['theory_title', 'theory_date']


admin.site.register(theory, theoryAdmin)

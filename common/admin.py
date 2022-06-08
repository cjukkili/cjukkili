from django.contrib import admin

# Register your models here.
from common.models import User, College, Gender, Calendar


class CalendarAdmin(admin.ModelAdmin):
    search_fields = ['content']
    list_display = ['content', 'start_date', 'end_date']


admin.site.register(User)
admin.site.register(College)
admin.site.register(Gender)
admin.site.register(Calendar,CalendarAdmin)


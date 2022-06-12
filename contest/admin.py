from django.contrib import admin

from contest.models import Contest


class ContestAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['id', 'name', 'registration_start_date', 'registration_end_date', 'contest_start_date',
                    'contest_end_date', 'site_url']


admin.site.register(Contest,ContestAdmin)
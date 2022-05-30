from django.contrib import admin

# Register your models here.
from common.models import User, College, Gender

admin.site.register(User)
admin.site.register(College)
admin.site.register(Gender)

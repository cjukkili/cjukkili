from django.contrib import admin

from board.models import Question, Comment, Category, BoardType


class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['title']


admin.site.register(Question, QuestionAdmin)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(BoardType)

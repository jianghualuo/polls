"""
这里使用 Django 自带的管理后台对数据库进行操作
这一代码中用到了 Django 的 admin 模块，将我们设计的问题和选项模型注册到后台，以便对数据进行后台的操作。
"""
from django.contrib import admin
from .models import Question, Choice
# Register your models here.


class ChoiceInline(admin.TabularInline):
    model = Choice


extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]


inlines = [ChoiceInline]
list_display = ('question_text', 'pub_date')
admin.site.register(Choice)
admin.site.register(Question, QuestionAdmin)

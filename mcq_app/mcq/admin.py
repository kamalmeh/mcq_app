from django.contrib import admin

from .models import Question, Test, Category, TestQuestion
admin.site.register(Question)
admin.site.register(Test)
admin.site.register(TestQuestion)
admin.site.register(Category)

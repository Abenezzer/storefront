from django.contrib import admin
from . import models
# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    readonly_fields = ['pub_date']  # Makes it visible as read-only

admin.site.register(models.Question, QuestionAdmin)


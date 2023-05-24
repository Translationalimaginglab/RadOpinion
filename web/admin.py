from . import models
from django.contrib import admin, auth


class ChoiceInLine(admin.TabularInline):
    model = models.Choice


class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInLine, ]


class MyAdminSite(admin.AdminSite):
    site_header = 'Decision Tree Questioner Administration'
    site_title = 'Administration'


admin_site = MyAdminSite()
# Register your models here.
admin_site.register(models.Choice)
admin_site.register(models.QuestionnaireItem)
admin_site.register(models.Question, QuestionAdmin)
admin_site.register(models.User, auth.admin.UserAdmin)
admin_site.register(models.Token)

from django.contrib import admin
from .models import FeedBackModels


class AdminForm(admin.ModelAdmin):
    list_display = ['Name', 'MailId', 'Msg']


admin.site.register(FeedBackModels, AdminForm)
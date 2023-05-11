from django.contrib import admin
from .models import Contact, Subscribe

admin.site.register(Contact)


@admin.register(Subscribe)
class SubscribeAdmin(admin.ModelAdmin):
    list_display = ['id', 'email']
    list_display_links = ['id', 'email']

from django.contrib import admin

from app.models import Client


class ClientAdmin(admin.ModelAdmin):
    list_display = ("pk", "first_name", "last_name", "phone", "price", "black_list", "addition", "updated")
    search_fields = ("first_name", "last_name", "addition", "updated", "phone")
    list_filter = ("first_name", "phone", "black_list")
    empty_value_display = "-пусто-"


admin.site.register(Client, ClientAdmin)

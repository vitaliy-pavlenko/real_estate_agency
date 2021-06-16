from django.contrib import admin

from .models import Complaint, Flat, Owner


class FlatAdmin(admin.ModelAdmin):
    search_fields = ['town', 'address', 'owner']
    readonly_fields = ['created_at']
    list_display = ['address', 'price', 'new_building', 'construction_year', 'town']
    list_editable = ['new_building']
    list_filter = ['new_building', 'rooms_number', 'floor']
    raw_id_fields = ['liked_by', 'owner']


class ComplaintAdmin(admin.ModelAdmin):
    list_display = ['author', 'flat', 'text']
    raw_id_fields = ['flat']


class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ['owner_flats']


admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Owner, OwnerAdmin)

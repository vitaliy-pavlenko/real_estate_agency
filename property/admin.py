from django.contrib import admin

from .models import Complaint, Flat, Owner


class OwnerInline(admin.TabularInline):
    model = Owner.flats.through
    raw_id_fields = ['owner']


class FlatAdmin(admin.ModelAdmin):
    search_fields = ['town', 'address']
    readonly_fields = ['created_at']
    list_display = ['address', 'price', 'new_building', 'construction_year', 'town']
    list_editable = ['new_building']
    list_filter = ['new_building', 'rooms_number', 'floor']
    raw_id_fields = ['liked_by']
    inlines = [OwnerInline]


class ComplaintAdmin(admin.ModelAdmin):
    list_display = ['author', 'flat', 'text']
    raw_id_fields = ['flat']


class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ['flats']


admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Owner, OwnerAdmin)

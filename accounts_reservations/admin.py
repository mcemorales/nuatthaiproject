from django.contrib import admin
from .models import account_reservation


class account_reservationAdmin(admin.ModelAdmin):
    list_display = ('massagetype', 'therapist', 'date', 'time',
                    'specialinstruction', 'mobile_number')
    list_filter = ('date', 'time',)
    search_fields = ('date', 'time',)
    list_per_page = 25


admin.site.register(account_reservation, account_reservationAdmin)

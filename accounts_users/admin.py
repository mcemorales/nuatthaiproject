from django.contrib import admin
from .models import account_user

class account_userAdmin(admin.ModelAdmin):
	list_display = ('id', 'first_name', 'last_name', 'username', 'email')
	list_filter = ('email',)
	search_fields = ('email', 'mobile_number', 'last_name',)
	list_per_page = 25

admin.site.register(account_user, account_userAdmin)
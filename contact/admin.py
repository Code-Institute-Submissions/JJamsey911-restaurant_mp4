# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.contrib import admin
from rangefilter.filters import DateRangeFilter

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Internal:
from .models import Contact

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# Registraion of the users contact information in the admin panel
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_filter = ("user", "name", "email", "phone", "date_created")
    list_display = ("message_id", "user", "name", "message", "phone", "date_created")

    search_fields = ["name"]
    list_filter = (("date_created", DateRangeFilter),)

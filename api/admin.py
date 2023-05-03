from django.contrib import admin
from api.models import Company, Employee


# Register your models here.
# customizing models ui here
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("name", "location", "type")
    # To search
    search_fields = ("name",)


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "company")
    list_filter = ("company",)


admin.site.register(Company, CompanyAdmin)
admin.site.register(Employee, EmployeeAdmin)

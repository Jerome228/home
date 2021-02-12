from django.contrib import admin
from .models import Expens, Salary

# Register your models here.
class ExpensAdmin(admin.ModelAdmin):
    fields = ("title", "amount", "person", "ddate",
              "comment")

admin.site.register(Expens, ExpensAdmin)

class SalaryAdmin(admin.ModelAdmin):
    fields = ("amount", "person", "ddate",
              "comment")

admin.site.register(Salary, SalaryAdmin)
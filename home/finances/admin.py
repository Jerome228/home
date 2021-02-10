from django.contrib import admin
from .models import Expens

# Register your models here.
class ExpensAdmin(admin.ModelAdmin):
    fields = ("title", "amount", "person", "ddate",
              "comment")


admin.site.register(Expens, ExpensAdmin)

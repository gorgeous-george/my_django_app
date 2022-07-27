from django.contrib import admin

from triangle.models import HistoryLog, Person


@admin.register(HistoryLog)
class HistoryLog(admin.ModelAdmin):
    list_filter = ['method', 'timestamp', 'path']


admin.site.register(Person)

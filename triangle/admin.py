from django.contrib import admin

from triangle.models import HistoryLog, Person

admin.site.register(HistoryLog)
admin.site.register(Person)

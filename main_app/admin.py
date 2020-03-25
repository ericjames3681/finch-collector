from django.contrib import admin

from .models import Record, Listening, Distributor
# Register your models here.

admin.site.register(Record)
admin.site.register(Listening)
admin.site.register(Distributor)

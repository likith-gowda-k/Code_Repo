from django.contrib import admin
from . models import Watches, WatchesUploads

# Register your models here.

admin.site.register(Watches)



class WatchUploadsAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'image')
    list_filter = ('name', 'price')
    search_fields= ('name', 'description')
    fields=  ['name', 'description', 'price', 'image']



admin.site.register(WatchesUploads, WatchUploadsAdmin)

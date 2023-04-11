from django.contrib import admin

# Register your models here.
from jobApp.models import hydjobs,lkojobs

class hydAdmin(admin.ModelAdmin):
    list_display=['id','company','address','email','phone','date']

class lkoAdmin(admin.ModelAdmin):
    list_display=['id','company','address','email','phone','date']

admin.site.register(hydjobs,hydAdmin)
admin.site.register(lkojobs,lkoAdmin)

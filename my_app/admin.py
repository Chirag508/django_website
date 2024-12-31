from django.contrib import admin
from .models import blog,contact,product
# Register your models here.

class blogadmin(admin.ModelAdmin):
    list_display = ('id','author','title','body','published_date')
    list_filter = ('published_date','title','author')
    search_fields = ('title','author')
    list_per_page = 15
    ordering = ('published_date',)

class contactadmin(admin.ModelAdmin):
    list_display = ('id','name','email','date_time','message')
    list_filter = ('date_time','name')
    search_fields = ('id','name','email')
    list_per_page = 15
    ordering = ('date_time',)

class productadmin(admin.ModelAdmin):
    list_display = ('id','name','details','price','quantity','Create_date','last_updated')
    list_filter = ('Create_date','name','price')
    search_fields = ('id','name','price')
    list_per_page = 15
    ordering = ('Create_date',)

admin.site.register(blog,blogadmin)
admin.site.register(contact,contactadmin)
admin.site.register(product,productadmin)
from django.contrib import admin
from .models import Car
from django.utils.html import format_html

# Register your models here.

class CarAdmin(admin.ModelAdmin):
  def thumbnail(self, object):
    return format_html('<img src="{}" width="40"/>'.format(object.car_photo.url))
  
    
  thumbnail.short_description = 'Car Image'

  list_display=('id','thumbnail','car_title','city','color','model','year','price','body_style','is_featured', 'is_published')
  list_display_links=('id','car_title','thumbnail')
  list_editable = ('is_featured','is_published')
  search_fields=('id','car_title','city','body_style', 'fuel_type')
  list_filter=('city','model','body_style','fuel_type')

admin.site.register(Car,CarAdmin)

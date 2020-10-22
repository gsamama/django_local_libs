from django.contrib import admin
from .models import Pictures

# Register your models here.

@admin.register(Pictures)
class PicuresAdmin(admin.ModelAdmin):
  list_display = ['pictureUrl']
  
  
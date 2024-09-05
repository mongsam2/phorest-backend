from django.contrib import admin
from .models import Gallery, Background, Category, ImageType

# Register your models here.
@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    pass

@admin.register(Background)
class BackgroundAdmin(admin.ModelAdmin):
    pass 

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(ImageType)
class ImageTypeAdmin(admin.ModelAdmin):
    pass
from django.contrib import admin

from .models import (
    AboutPageContent,
    AboutPageImage,
    Application,
    HomePageContent,
    HomePageImage,
    Image,
    Service
)


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'email')
    search_fields = ('name', 'email', 'phone_number')
    list_filter = ()


class HomePageImageInline(admin.TabularInline):
    model = HomePageImage
    extra = 1


@admin.register(HomePageContent)
class HomePageContentAdmin(admin.ModelAdmin):
    list_display = ('title',)
    inlines = [HomePageImageInline]


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'image')
    search_fields = ('name', 'description')
    list_filter = ('name',)


class AboutPageImageInline(admin.TabularInline):
    model = AboutPageImage
    extra = 1


@admin.register(AboutPageContent)
class AboutPageContentAdmin(admin.ModelAdmin):
    list_display = ('title',)
    inlines = [AboutPageImageInline]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_at')
    search_fields = ('title', 'caption')
    ordering = ('-uploaded_at',)

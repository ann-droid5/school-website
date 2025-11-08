from django.contrib import admin
from .models import (
    HeroSlide, AboutSection, StudentLife, NewsArticle,
    GalleryImage, Footer, FooterLinkCategory, FooterLink
)

# Inline link management for footer
class FooterLinkInline(admin.TabularInline):
    model = FooterLink
    extra = 1


class FooterLinkCategoryAdmin(admin.ModelAdmin):
    inlines = [FooterLinkInline]


admin.site.register(HeroSlide)
admin.site.register(AboutSection)
admin.site.register(StudentLife)
admin.site.register(NewsArticle)
admin.site.register(GalleryImage)
admin.site.register(Footer)
admin.site.register(FooterLinkCategory, FooterLinkCategoryAdmin)

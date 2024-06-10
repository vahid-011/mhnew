from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import News

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'updated_date', 'updated_time')
    readonly_fields = ('photo_count',)
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'updated_time', 'updated_date')
        }),
        ('Photos', {
            'fields': ('photo', 'photo_count'),
            'classes': ('collapse',),
            'description': 'Maximum 15 photos allowed.',
        }),
    )

admin.site.register(News, NewsAdmin)
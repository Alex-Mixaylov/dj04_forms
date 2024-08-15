from django.contrib import admin
from django.utils.html import format_html
from .models import Movie

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_date', 'review', 'poster_preview')
    search_fields = ('title', 'description')
    list_filter = ('release_date',)

    def poster_preview(self, obj):
        if obj.poster:
            return format_html('<img src="{}" width="100" />', obj.poster.url)
        return "Нет изображения"
    poster_preview.short_description = "Превью постера"

    # Убедитесь, что поле poster доступно для редактирования
    fields = ('title', 'poster', 'description', 'release_date', 'review')

admin.site.register(Movie, MovieAdmin)

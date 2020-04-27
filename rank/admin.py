from django.contrib import admin

from .models import Score


class ScoreAdmin(admin.ModelAdmin):
    list_display = ['client', 'score']


admin.site.register(Score)

from django.contrib import admin
from .models import *


class FighterAdmin(admin.ModelAdmin):
    list_display = ('alias', 'force', 'skill', 'resistance', 'avatar')
    search_fields = ('alias',)


class TournamentAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'finish_date', 'fighter_count', 'category')
    list_filter = ('start_date', 'finish_date', 'fighter_count', 'category')
    search_fields = ('name',)
    filter_horizontal = ('fighters',)


class CombatAdmin(admin.ModelAdmin):
    list_display = ('date', 'fighter1', 'fighter2', 'tournament')
    list_filter = ('tournament', 'fighter1', 'fighter2')


admin.site.register(Fighter, FighterAdmin)
admin.site.register(Tournament, TournamentAdmin)
admin.site.register(Combat, CombatAdmin)

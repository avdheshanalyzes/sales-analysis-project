from django.contrib import admin
from .models import Player, Match, Performance, Contribution

admin.site.register(Player)
admin.site.register(Match)
admin.site.register(Performance)
admin.site.register(Contribution)

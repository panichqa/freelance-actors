from django.contrib import admin

from .models import Actor, Agency, Character, ActorAgency


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ("username", "first_name", "last_name", "gender")
    search_fields = ("username", "first_name", "last_name")


@admin.register(Agency)
class AgencyAdmin(admin.ModelAdmin):
    list_display = ("name", "city")
    search_fields = ("name", "city")


@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ("name", "gender", "agency")
    search_fields = ("name",)


@admin.register(ActorAgency)
class ActorAgencyAdmin(admin.ModelAdmin):
    list_display = ('actor', 'character', 'agency', 'is_booked')
    list_filter = ('is_booked',)

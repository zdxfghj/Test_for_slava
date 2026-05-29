from django.contrib import admin

from .models import Person, Card


class PersonAdmin(admin.ModelAdmin):
    list_display = ["name", "year", "answer", "wentToLink", "takeCardNumber",
                    "takeCardCVV", "takeCardFIO", "takeCardDATE"]
    list_filter = ["year", "wentToLink", "takeCardNumber", "takeCardCVV", "takeCardFIO", "takeCardDATE"]
    list_display_links = ('name',)


class CardAdmin(admin.ModelAdmin):
    list_display = ['number', 'nameBank', 'system']


admin.site.register(Person, PersonAdmin)
admin.site.register(Card, CardAdmin)

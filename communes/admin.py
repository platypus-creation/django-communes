from django.contrib import admin
from django.contrib.gis.admin.options import GeoModelAdmin
from django.conf import settings

from communes.models import Commune

class CommuneAdmin(GeoModelAdmin):
    search_fields = ('name',)
    order = 1
    list_per_page = 300

admin.site.register(Commune, CommuneAdmin)
# admin.site.register(Commune)
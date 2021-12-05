

from django.contrib import admin
from .models import *

class DocProfileAdmin(admin.ModelAdmin):
    model = DocProfile
    #list_display = ('UserID', 'specialization', 'location', )

admin.site.register(DocProfile, DocProfileAdmin)
admin.site.register(Specialization)
admin.site.register(Location)

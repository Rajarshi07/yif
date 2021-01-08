from django.contrib import admin

from .models import Member,Position,State,Society,Initiative,Contact,Circular,NEW,Outreach,File

# Register your models here.

admin.site.register(Member)
admin.site.register(State)
admin.site.register(Outreach)
admin.site.register(Society)
admin.site.register(Initiative)
admin.site.register(Position)
admin.site.register(Contact)
admin.site.register(Circular)
admin.site.register(NEW)
admin.site.register(File)
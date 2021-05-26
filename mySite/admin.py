from django.contrib import admin
from mySite.models import makeEvent
from mySite.models import myEvent,cordinator


# Register your models here.
admin.site.register(makeEvent)
admin.site.register(myEvent)
admin.site.register(cordinator)
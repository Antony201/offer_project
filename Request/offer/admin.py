from django.contrib import admin

from .models import Client, Responsible, Offer


admin.site.register(Client)
admin.site.register(Responsible)
admin.site.register(Offer)
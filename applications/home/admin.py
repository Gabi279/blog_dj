from django.contrib import admin

from applications.home.models import Home, Suscribers, Contact

# Register your models here.

admin.site.register(Home)
admin.site.register(Suscribers)
admin.site.register(Contact)

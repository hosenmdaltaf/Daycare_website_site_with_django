from django.contrib import admin
from classes.models import Services,Gallery, Slider,Contact,Service_add

# Register your models here.
admin.site.register(Services)

admin.site.register(Slider)

admin.site.register(Gallery)
admin.site.register(Contact)
admin.site.register(Service_add)
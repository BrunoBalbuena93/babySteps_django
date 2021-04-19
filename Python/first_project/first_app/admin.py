from django.contrib import admin
from first_app.models import Topic, AccessRecord, Webpage, UserProfileInfo
# Register your models here.
# Agregando la tabla AccessRecord
admin.site.register(AccessRecord)
# Agregando la tabla Topic
admin.site.register(Topic)
# Agregando la tabla Webpage
admin.site.register(Webpage)
# Agregando el usuario
admin.site.register(UserProfileInfo)
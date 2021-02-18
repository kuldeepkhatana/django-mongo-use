from django.contrib import admin
from odata.models import *
from django.contrib.auth.models import Group, User

# Register your models here.

admin.site.register(Tutorial)

# UnRegister your model.
admin.site.unregister(User)
admin.site.unregister(Group)
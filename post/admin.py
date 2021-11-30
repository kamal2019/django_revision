from django.contrib import admin
from . models import Posts
from . models import organizations
# Register your models here.

admin.site.register(Posts)
admin.site.register(organizations)
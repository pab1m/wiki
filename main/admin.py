from django.contrib import admin
from .models import Authors
from .models import About

admin.site.register(Authors)
admin.site.register(About)

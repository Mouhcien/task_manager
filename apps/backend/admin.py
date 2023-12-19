from django.contrib import admin

from .models import Project, Function, Phase

admin.site.register(Project)
admin.site.register(Phase)
admin.site.register(Function)
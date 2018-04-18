from django.contrib import admin

# Register your models here.
# Lets admin know Question objects have admin interface

from .models import Question

admin.site.register(Question)

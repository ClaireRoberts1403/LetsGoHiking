from django.contrib import admin
from .models import category, product


admin.site.register(product)
admin.site.register(category)

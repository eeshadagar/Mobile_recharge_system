from django.contrib import admin

from .models import Payments_post, Payments_pre

# Register your models here.

admin.site.register(Payments_pre)
admin.site.register(Payments_post)
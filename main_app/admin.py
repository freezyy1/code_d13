from django.contrib import admin
from .models import Category, Advert, Announcer, Reply


admin.site.register(Advert)
admin.site.register(Announcer)
admin.site.register(Category)
admin.site.register(Reply)

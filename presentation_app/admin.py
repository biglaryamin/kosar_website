from django.contrib import admin
from . import models


admin.site.register(models.Products)
admin.site.register(models.ImageModel)
admin.site.register(models.TextModel)
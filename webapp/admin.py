from django.contrib import admin

from .models import Group
from .models import Painting
from .models import Painter


admin.site.register(Group)
admin.site.register(Painting)
admin.site.register(Painter)

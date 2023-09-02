from django.contrib import admin

from .models import Category
from .models import Topping
from .models import IceCream
from .models import Wrapper

admin.site.register(Category)
admin.site.register(Topping)
admin.site.register(IceCream)
admin.site.register(Wrapper)
from django.contrib import admin

# Register your models here.
# from .models import RegistrationForm
from .models import Marks,Registration

# mymodels = [Marks,Registration]
# admin.site.register(mymodels)

admin.register(Marks, Registration)(admin.ModelAdmin)

# admin.site.register(RegistrationForm)
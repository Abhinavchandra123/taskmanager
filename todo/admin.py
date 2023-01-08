from django.contrib import admin
# Register your models here.
from .models import *

admin.site.register(Employee)
admin.site.register(Job)
admin.site.register(Count)
admin.site.register(Branch)
admin.site.register(Thought)
admin.site.register(Strategy)
admin.site.register(Operation)
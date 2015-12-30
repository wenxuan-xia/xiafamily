from django.contrib import admin
from .models import *
# Register your models here.

class familyMemberAdmin(admin.ModelAdmin):
    list_display = familyMember._meta.get_all_field_names()


admin.site.register(familyMember, familyMemberAdmin)
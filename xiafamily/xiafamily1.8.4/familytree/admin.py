from django.contrib import admin
from .models import *
# Register your models here.

class familyMemberAdmin(admin.ModelAdmin):
    list_display = ["oldsystem_id", "name", "gender", "generation", "belongs_to"]


admin.site.register(familyMember, familyMemberAdmin)
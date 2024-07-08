from django.contrib import admin
from django.urls import path
from App1.views import IndexView
from .models import AutorDb, FraseDb


# Register your models here.
admin.site.site_header = "hola"



class FraseInline(admin.TabularInline):
    model = FraseDb
    extra = 1

class AutorAdmin(admin.ModelAdmin):
    fields = ["nombre", "fecha_nacimiento", "fecha_fallecimiento", "profesion","nacionalidad"]
    list_display = ["nombre", "fecha_nacimiento"]

    inlines = [FraseInline]

                

admin.site.register(AutorDb, AutorAdmin)

class FraseAdmin(admin.ModelAdmin):
    fields = ["cita", "autor_fk"]
    list_display = ["cita"]

@admin.register(FraseDb)
class FraseAdmin(admin.ModelAdmin):
    fields = ["cita", "autor_fk"]
    list_display = ["cita"]
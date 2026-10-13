from django.contrib import admin
import libreria.models as models
# Register your models here.
admin.site.register(models.Editorial)

class EditorialAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'Localidad', 'email', 'cedes')
    list_filter = ('Localidad',)

admin.site.register(models.Libro)

class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'editorial', 'costo', 'descripcion')
    list_filter = ('titulo', 'editorial', 'costo')

@admin.display(description='Costo', ordering='costo')
def costo(self, obj):
        return f"$ {obj.costo:,0f}".replace(',', '.')

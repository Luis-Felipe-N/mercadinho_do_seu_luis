from django.contrib import admin
from users.models import *
from django.contrib.auth.admin import UserAdmin


# Register your models here.
@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):

    add_fieldsets = (
        (None, {
            "fields": (
               "is_vendedor" 
            ),
        }),
    )


@admin.register(Vendedor)
class VendedorAdmin(admin.ModelAdmin):
    pass


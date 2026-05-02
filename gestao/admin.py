from django.contrib import admin
from .models import Usuarios, Imoveis, FotosImoveis, Chaves, Historico

admin.site.register(Usuarios)
admin.site.register(Imoveis)
admin.site.register(FotosImoveis)
admin.site.register(Chaves)
admin.site.register(Historico)



# Register your models here.

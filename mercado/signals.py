from django.db.models.signals import pre_save

from users.models.Vendedor import Vendedor
from users.models.Usuario import Usuario
from django.db.models.signals import pre_save

def criar_vendedor(sender, **kwargs):
    # usuario = Usuario.objects.get(id=sender.usuario.id)

    print(f'Criando vendedor ligado ao usuário [user]')


pre_save.connect(criar_vendedor, sender=Vendedor)
    
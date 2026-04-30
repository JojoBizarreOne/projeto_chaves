from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuarios(AbstractUser):
    class Tipos(models.TextChoices):
        ADMINISTRADOR = 'ADM', 'Administrador'
        COLABORADOR = 'COL', 'Colaborador'
        PROPRIETARIO = 'PRP', 'Proprietário'
        CLIENTE = 'CLI', 'Cliente'
    CPF = models.CharField(max_length=11, primary_key=True)
    celular = models.CharField("Celular", max_length=11, unique=True)
    contato = models.CharField("Contato",max_length=11, blank=True)
    email = models.EmailField("E-mail", unique=True)
    endereco = models.CharField("Endereço", max_length=100)
    tipo = models.CharField("Tipo", max_length=3, choices=Tipos.choices, default=Tipos.CLIENTE)
    observacoes = models.TextField("Observações", blank=True, null=True)
    foto = models.ImageField("Foto", upload_to='usuarios/', blank=True, null=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} ({self.get_tipo_display()})"

class Chaves(models.Model):
    codigo = models.CharField("Código", primary_key=True)
    imovel = models.ForeignKey(on_delete=models.CASCADE, Model=Imoveis.endereco)
    esta_disponivel = models.BooleanField(default=True)
    usuario_retirada = models.ForeignKey('Usuarios', on_delete=models.CASCADE, blank=True, null=True)
    data_retirada = models.DateTimeField()

class Imoveis(models.Model):
    endereco = models.CharField("Endereço", primary_key=True)
    proprietario = models.ForeignKey(on_delete=CASCADE, )
# Create your models here.

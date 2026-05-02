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

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.get_tipo_display()})"

class Imoveis(models.Model):
    rua = models.CharField("Endereço", max_length=100)
    numero = models.CharField("Número", max_length=6)
    bairro = models.CharField("Bairro", max_length=100)
    cidade = models.CharField("Cidade", max_length=100)
    estado = models.CharField("Estado", max_length=100)
    proprietario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    observacao = models.TextField("Observações", blank=True)
    data_criacao = models.DateField("Data de Cadastro", auto_now_add=True)
    data_atualizacao = models.DateTimeField("Última Atualização", auto_now=True)

    class Meta:
        constraints = [models.UniqueConstraint (fields=['rua', 'numero', 'bairro', 'cidade', 'estado'], name='endereco')]
        verbose_name = "Imóvel"
        verbose_name_plural = "Imóveis"
 

    def __str__(self):
        return f"{self.rua}, {self.numero}, {self.bairro}, {self.cidade}-{self.estado}"

class FotosImoveis(models.Model):
    imovel = models.ForeignKey(Imoveis, on_delete=models.CASCADE, related_name='fotos')
    foto = models.ImageField("Foto", upload_to="imoveis/", blank=True, null=True)
    descricao = models.CharField("Descrição", max_length=100, blank=True)

    class Meta:
        verbose_name = "Foto do Imóvel"
        verbose_name_plural = "Fotos dos Imóvel"

class Chaves(models.Model):
    codigo = models.CharField("Código", primary_key=True)
    imovel = models.ForeignKey(Imoveis, on_delete=models.CASCADE)
    esta_disponivel = models.BooleanField("Disponibilidade", default=True)
    usuario_açao = models.ForeignKey(Usuarios, on_delete=models.CASCADE, blank=True)
    data_ação= models.DateTimeField("Data", auto_now=True)

    class Meta:
        verbose_name = "Chave"
        verbose_name_plural = "Chaves"
    def __str__(self):
        return f"{self.codigo} - {self.imovel} - {self.esta_disponivel}"

class Historico(models.Model):
    usuario = models.ForeignKey(Usuarios, on_delete=models.SET_NULL, null=True)
    chave = models.ForeignKey(Chaves, on_delete=models.PROTECT)        
    time_stamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Histórico"
        verbose_name_plural = "Histórico"
    


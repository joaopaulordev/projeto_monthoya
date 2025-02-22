from django.db import models
from datetime import datetime
from django.utils.html import format_html

# Create your models here.

class Funcionario(models.Model):
    nome = models.CharField(max_length=300, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    foto = models.ImageField(null=False, blank=False, default='user-default.png')
    cargo = models.CharField(max_length=200, null=True, blank=True)
    descricao = models.TextField()

    class Meta:
        verbose_name = "Funcionário"
        verbose_name_plural = "Funcionários"

    def __str__(self):
        return f'{self.nome} | {self.cargo} | {self.email}'


class Bairro(models.Model):
    descricao = models.CharField(max_length=600, null=True, blank=True)
    isHomepage = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Bairro"
        verbose_name_plural = "Bairros"

    def __str__(self):
        return f'{self.descricao}'
    


TIPOS = (
    ('Apartamento', 'Apartamento'),
    ('Casa/Sobrado', 'Casa/Sobrado'),
    ('Terreno', 'Terreno')
)

OBJETIVOS = (
    ('VENDA', 'VENDA'), 
    ('ALUGA', 'ALUGA')
)

class Imovel(models.Model):
    thumbnail = models.ImageField(null=True, blank=True)
    titulo = models.CharField(max_length=600, null=True, blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    tipo = models.CharField(max_length=100, null=True, blank=True, choices=TIPOS)
    objetivo = models.CharField(max_length=50, null=True, blank=True, choices=OBJETIVOS)
    ativo = models.BooleanField(default=True)
    destaque = models.BooleanField(default=False)
    views = models.IntegerField(default=0)
    data_criacao = models.DateTimeField(null=True, blank=True, default=datetime.now())
    bairro = models.ForeignKey(Bairro, null=True, blank=True, on_delete=models.SET_NULL)
    endereco = models.CharField(max_length=600, null=True, blank=True)
    cidade = models.CharField(max_length=200, null=True, blank=True, default='Paranavaí-PR')
    descricao = models.TextField(null=True, blank=True)
    qtde_quartos = models.IntegerField(default=0)
    qtde_suites = models.IntegerField(default=0)
    qtde_banheiros = models.IntegerField(default=0)
    qtde_vagas = models.IntegerField(default=0)
    qtde_vagas_coberta = models.IntegerField(default=0)
    area_total = models.IntegerField(default=0)
    area_construida = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Imóvel"
        verbose_name_plural = "Imóveis"

    def __str__(self):
        return self.titulo
    

class ImovelFoto(models.Model):
    imagem = models.ImageField(null=True, blank=True)
    imovel = models.ForeignKey(Imovel, null=True, blank=True, on_delete=models.CASCADE)
    
    def image_tag(self):
         return format_html('<img src="{}" style="max-width:100px; max-height:100px"/>'.format(self.imagem.url))


STATUS = (
    ("RESPONDER", "RESPONDER"),
    ("RESPONDIDO", "RESPONDIDO"),
)

class ImovelContato(models.Model):
    imovel = models.ForeignKey(Imovel, null=True, blank=True, on_delete=models.CASCADE)
    nome = models.CharField(max_length=200, null=True, blank=True)
    assunto = models.CharField(max_length=300, null=True, blank=True)
    telefone = models.CharField(max_length=20, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    mensagem = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=20, null=True, blank=True, choices=STATUS, default="RESPONDER")
    data_criacao = models.DateTimeField(null=True, blank=True, default=datetime.now())

    class Meta:
        verbose_name = "Contato pelo Imóvel"
        verbose_name_plural = "Contatos pelo Imóveis"
    
    def __str__(self):
        return '' #'Título: {}, Preço: {}, Objetivo: {}, Tipo: {} '.format(self.imovel.titulo, self.imovel.preco, self.imovel.objetivo, self.imovel.tipo)



class Contato(models.Model):
    nome = models.CharField(max_length=300, null=True, blank=True)  
    email = models.CharField(max_length=200, null=True, blank=True)
    assunto = models.CharField(max_length=300, null=True, blank=True)
    telefone = models.CharField(max_length=20, null=True, blank=True)
    mensagem = models.TextField()
    status = models.CharField(max_length=20, null=True, blank=True, choices=STATUS, default="RESPONDER")
    data_criacao = models.DateTimeField(null=True, blank=True, default=datetime.now())

    class Meta:
        verbose_name = "Contato"
        verbose_name_plural = "Contatos"

    def __str__(self):
        return ''
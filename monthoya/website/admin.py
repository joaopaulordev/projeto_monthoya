from django.contrib import admin
from .models import *
from django.urls import reverse
from django.utils.html import format_html, urlencode
from django.utils.safestring import mark_safe

from django.forms import TextInput, Textarea
# import locale


@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ("nome", "cargo", "descricao", "email", "image_tag",)
    
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'90'})},
        models.TextField: {'widget': Textarea(attrs={'rows':6, 'cols':92})},
    }

    def image_tag(self, obj):
        return format_html('<img src="{}" style="max-width:50px; max-height:50px"/>'.format(obj.foto.url))
    image_tag.short_description = 'Foto'


@admin.register(Bairro)
class BairroAdmin(admin.ModelAdmin):
    list_display = ("descricao", "isHomepage", )
    search_fields = ["descricao"]
    
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'90'})},
    }


@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    list_display = ("nome", "assunto", "mensagem", "data_criacao", "whatsapp_tag", "status")  
    list_filter = ["status"]
    actions=['contact_open','contact_close']
    search_fields = ["nome"]
    # search_help_text = "Pesquise pelo nome da pessoa"

    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'90'})},
        models.TextField: {'widget': Textarea(attrs={'rows':6, 'cols':92})},
    }

    def whatsapp_tag(self, obj):
        return format_html('<a href="https://wa.me/55{}" target="_blank">{}</a>'.format(obj.telefone, obj.telefone))
    whatsapp_tag.short_description = 'Whatsapp'
    
    @admin.action(description='RESPONDER')
    def contact_open(self, request, queryset):
        queryset.update(status='RESPONDER')

    @admin.action(description='RESPONDIDO')
    def contact_close(self, request, queryset):
        queryset.update(status='RESPONDIDO')


@admin.register(ImovelContato)
class ImovelContatoAdmin(admin.ModelAdmin):
    list_display = ("nome", "assunto", "mensagem", "view_imovel_link", "data_criacao", "whatsapp_tag", "status")  
    list_filter = ["status"]
    actions=['contact_open','contact_close']
    search_fields = ["nome"]

    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'90'})},
        models.TextField: {'widget': Textarea(attrs={'rows':6, 'cols':92})},
    }

    def whatsapp_tag(self, obj):
        return format_html('<a href="https://wa.me/55{}" target="_blank">{}</a>'.format(obj.telefone, obj.telefone))
    whatsapp_tag.short_description = 'Whatsapp'

    def view_imovel_link(self, obj):
        url = reverse("admin:website_imovel_change", args=[obj.imovel.id]) + '?_popup=1'        
        link = '<a href="%s" target="_blank">%s</a>' % (url, obj.imovel.titulo)
        return mark_safe(link)
    view_imovel_link.short_description = 'Imóvel'

    @admin.action(description='RESPONDER')
    def contact_open(self, request, queryset):
        queryset.update(status='RESPONDER')

    @admin.action(description='RESPONDIDO')
    def contact_close(self, request, queryset):
        queryset.update(status='RESPONDIDO')




class ImovelFotoInline(admin.TabularInline):
    model = ImovelFoto
    readonly_fields = ('id', 'image_tag',)
    extra = 0
    classes = ('collapse', )
                                  
@admin.register(Imovel)
class ImovelAdmin(admin.ModelAdmin):
    list_display = ("titulo", "ativo", "views", "destaque", "formatted_price", "objetivo", "tipo", "data_criacao", )
    list_filter = ["ativo", "objetivo", "destaque", "tipo",]
    search_fields = ["titulo"]
    actions=['imovel_ativar','imovel_desativar', "destaque_ativar", "destaque_desativar"]
    fields = ["thumbnail", "titulo", "preco", "objetivo", "tipo", ("ativo", "destaque", "views"), 
              "data_criacao", "bairro", "endereco", "cidade", "descricao",
              ("qtde_quartos", "qtde_suites", "qtde_banheiros"),
              ("qtde_vagas", "qtde_vagas_coberta"),
              ("area_total", "area_construida")
    ]    
    inlines = [ImovelFotoInline]

    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'90'})},
        models.TextField: {'widget': Textarea(attrs={'rows':6, 'cols':92})},
    }

    @admin.action(description='Ativar imóveis selecionados')
    def imovel_ativar(self, request, queryset):
        queryset.update(ativo=True)

    @admin.action(description='Desativar imóveis selecionados')
    def imovel_desativar(self, request, queryset):
        queryset.update(ativo=False)

    @admin.action(description='Ativar destaque imóveis selecionados')
    def destaque_ativar(self, request, queryset):
        queryset.update(destaque=True)

    @admin.action(description='Desativar destaque imóveis selecionados')
    def destaque_desativar(self, request, queryset):
        queryset.update(destaque=False)

    class Media:
        js = ['js/list_filter_collapse_imovel.js']      

    
    def formatted_price(self, obj):
        return 'R${}'.format(obj.preco)
    formatted_price.short_description = 'Preço'

    # def formatted_price(self, obj):
    #     locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    #     valor = locale.currency(obj.preco, grouping=True, symbol=None)
    #     return 'R${}'.format(valor)
    # formatted_price.short_description = 'Preço'

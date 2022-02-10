from django.db import models
from stdimage.models import StdImageField

from django.db.models import signals
from django.template.defaultfilters import slugify


# Create your models here.

class Base(models.Model):
    criado = models.DateField('Data de Criação', auto_now_add=True)
    modificado = models.DateField('Data de Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True


class Cliente(Base):
    nome = models.CharField('Nome', max_length=100)
    telefone = models.CharField('Telefone', max_length=100)
    dataNascimento = models.DateField('Data de Nascimento')
    imagem = StdImageField('Imagem', upload_to='clientes', variations={'thumb': (124, 124)}, default="none")
    slug = models.SlugField('Slug', max_length=100, blank=True, editable=False)

    def __str__(self):
        return self.nome


def cliente_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.nome)


signals.pre_save.connect(cliente_pre_save, sender=Cliente)


class Servico(Base):
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preço', max_digits=5, decimal_places=2)

    def __str__(self):
        return self.nome

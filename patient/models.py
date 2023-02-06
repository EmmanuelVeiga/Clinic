from django.db import models


class Paciente(models.Model):
    Nome = models.CharField(max_length=100, )
    Gênero = models.CharField(max_length=100, verbose_name='Sexo')
    Estado_Civil = models.CharField(max_length=100, verbose_name='Estado civil')
    Data_Nascimento = models.DateField(max_length=100, )
    Naturalidade = models.CharField(max_length=100, verbose_name='Cidade Nascimento')
    Estado_Nascimento = models.CharField(max_length=100, verbose_name='Estado Nascimento')
    Profissão = models.CharField(max_length=100, blank=True, null=True)
    CPF = models.CharField(max_length=100, )
    Religião = models.CharField(max_length=100, blank=True, null=True)
    Telefone = models.CharField(max_length=100)
    Mãe = models.CharField(max_length=100, blank=True, null=True)
    Pai = models.CharField(max_length=100, blank=True, null=True)
    Cep = models.CharField(max_length=100, )
    Rua_avenida = models.CharField(max_length=100, )
    Número = models.CharField(max_length=100, )
    Complemento = models.CharField(max_length=100, )
    Bairro = models.CharField(max_length=100, )
    Cidade = models.CharField(max_length=100, )
    Estado = models.CharField(max_length=100, )
    Convênio = models.CharField(max_length=100, )
    Plano = models.CharField(max_length=100, blank=True, null=True)
    Cartão = models.CharField(max_length=100, blank=True, null=True)
    Data_vencimento = models.DateField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f'{self.Nome} - {self.Telefone}'

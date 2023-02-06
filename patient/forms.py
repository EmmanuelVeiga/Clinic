from django import forms

from patient.models import Paciente


class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        exclude = ()

        widgets = {
            'Nome': forms.TextInput(attrs={'class': 'form-control'}),
            'Gênero': forms.TextInput(attrs={'class': 'form-control'}),
            'Estado_Civil': forms.TextInput(attrs={'class': 'form-control'}),
            'Data_Nascimento': forms.DateInput(attrs={'class': 'form-control'}),
            'Naturalidade': forms.TextInput(attrs={'class': 'form-control'}),
            'Estado_Nascimento': forms.TextInput(attrs={'class': 'form-control'}),
            'Profissão': forms.TextInput(attrs={'class': 'form-control'}),
            'CPF': forms.NumberInput(attrs={'class': 'form-control'}),
            'Religião': forms.TextInput(attrs={'class': 'form-control'}),
            'Telefone': forms.NumberInput(attrs={'class': 'form-control'}),
            'Mãe': forms.TextInput(attrs={'class': 'form-control'}),
            'Pai': forms.TextInput(attrs={'class': 'form-control'}),
            'Cep': forms.NumberInput(attrs={'class': 'form-control'}),
            'Rua_avenida': forms.TextInput(attrs={'class': 'form-control'}),
            'Número': forms.TextInput(attrs={'class': 'form-control'}),
            'Complemento': forms.TextInput(attrs={'class': 'form-control'}),
            'Bairro': forms.TextInput(attrs={'class': 'form-control'}),
            'Cidade': forms.TextInput(attrs={'class': 'form-control'}),
            'Estado': forms.TextInput(attrs={'class': 'form-control'}),
            'Convênio': forms.TextInput(attrs={'class': 'form-control'}),
            'Plano': forms.TextInput(attrs={'class': 'form-control'}),
            'Cartão': forms.TextInput(attrs={'class': 'form-control'}),
            'Data_vencimento': forms.DateInput(attrs={'class': 'form-control'}),

        }

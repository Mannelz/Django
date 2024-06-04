from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(label='', max_length=20, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nome'}))
    
    last_name = forms.CharField(label='', max_length=50, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Sobrenome'}))
    
    username = forms.CharField(label='', max_length=20, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nome de usuário', 'help_text':'<span class="form-text text-muted"><small>Required. No máximo 20 caracteres. Apenas letras, digitos e @/./+/-/_.</small></span>'}))
    
    email = forms.EmailField(label='', max_length=50, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email'}))
    
    password1 = forms.CharField(label='', max_length=20, widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Senha'}), help_text='<ul class="form-text text-muted small"><li>Sua senha não pode ser igual a suas informações pessoais.</li><li>Sua senha deve conter no mínimo 8 caracteres.</li><li>Sua senha não pode ser uma senha comum.</li><li>Sua senha não pode conter apenas números.</li></ul>')
    
    password2 = forms.CharField(label='', max_length=20, widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Confirme sua senha'}), help_text='<span class="form-text text-muted"><small>As senhas devem ser iguias.</small></span')

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

class AddRecordForm(forms.ModelForm):
    first_name = forms.CharField(required=True, label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nome'}))
    last_name = forms.CharField(required=True, label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Sobrenome'}))
    email = forms.EmailField(required=True, label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email'}))
    phone = forms.CharField(required=True, label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Telefone'}))
    address = forms.CharField(required=True, label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Endereço'}))
    city = forms.CharField(required=True, label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Cidade'}))
    state = forms.CharField(required=True, label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Estado'}))
    zipcode = forms.CharField(required=True, label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'CEP'}))

    class Meta:
        model = Record
        exclude = ('user',)
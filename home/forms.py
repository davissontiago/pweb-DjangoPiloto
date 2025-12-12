from django import forms
    
class ContatoForm(forms.Form):
    
    nome = forms.CharField(
        max_length=100, 
        label='Nome Completo',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome completo'})
    )
    
    telefone = forms.CharField(
        label='Telefone/WhatsApp',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(00) 00000-0000'})
    )
    
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'E-mail'})
    )
    
    categoria = forms.ChoiceField(
        label='Assunto de Contato',
        choices=[
            ('suporte', 'Suporte Técnico'),
            ('comercial', 'Comercial'),
            ('reclamacao', 'Reclamação'),
            ('parceria', 'Parceria'),
            ('financeiro', 'Financeiro')
        ],
        widget=forms.Select(attrs={'class': 'form-select'}) 
    )
    
    mensagem = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Escreva sua mensagem', 'rows': 2})
    )

class ProdutoForm(forms.Form):
    nome = forms.CharField(
        max_length=100,
        label='Nome do Produto',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do Produto'})
    )
    
    preco = forms.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        label='Preço',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Preço'})
    )
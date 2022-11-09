#LOS FORMULARIOS DE DJANGO SON CLASES

from django import forms


class FormularioEmpleados(forms.Form):

    #CREANDO ATRIBUTO PARA ACRGAR EL SELECTOR
    OPCIONES=(
        (1,'Cocinero'),
        (2,'Ayudante'),
        (3,'Mesero'),
        (4,'Administrador')
    )

    #DENTRO DE LA CLASE CADA ATRIBUTO SERÁ UN INPUT

    nombresEmpleado=forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control mb-3'}),
        required=True,
        max_length=50,
        label="Nombres"
    )
    
    apellidosEmpleado=forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control mb-3'}),
        required=True,
        max_length=50,
        label="Apellidos"
    )

    fotoEmpleado=forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control mb-3'}),
        required=True,
        label="Foto"
    )

    cargo=forms.ChoiceField(
        widget=forms.Select(attrs={'class':'form-control mb-3'}),
        required=True,
        choices=OPCIONES,
        label="Cargo"
    )
    
    salario=forms.CharField(
        widget=forms.NumberInput(attrs={'class':'form-control mb-3'}),
        required=True,
        label="Salario"
    )
    
    telefono=forms.CharField(
        widget=forms.NumberInput(attrs={'class':'form-control mb-3'}),
        required=True,
        label="Número de contacto"
    )
    
    
#LOS FORMULARIOS DE DJANGO SON CLASES

from django import forms


class FormularioPlatos(forms.Form):

    #CREANDO ATRIBUTO PARA ACRGAR EL SELECTOR
    OPCIONES=(
        (1,'Entrada'),
        (2,'Plato fuerte'),
        (3,'Postre')
    )

    #DENTRO DE LA CLASE CADA ATRIBUTO SERÁ UN INPUT

    nombrePlato=forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control mb-3'}),
        required=True,
        max_length=50,
        label="Nombre del plato"
    )

    descripcionPlato=forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control mb-3'}),
        required=False,
        max_length=200,
        label="Descripción del plato"
    )

    fotoPlato=forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control mb-3'}),
        required=True,
        label="Foto del plato"
    )

    precioPlato=forms.CharField(
        widget=forms.NumberInput(attrs={'class':'form-control mb-3'}),
        required=True,
        label="Precio"
    )
    
    tipoPlato=forms.ChoiceField(
        widget=forms.Select(attrs={'class':'form-control mb-3'}),
        required=True,
        choices=OPCIONES,
        label="Tipo de plato"
    )
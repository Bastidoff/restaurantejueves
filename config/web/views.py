from django.shortcuts import render


#IMPORTAR EL FORMULARIO A RENDER
from web.formularios.formularioPlatos import FormularioPlatos
from web.formularios.formularioEmpleados import FormularioEmpleados

# Create your views here.
#las vistas en djangp son los CONTROLADORES

#las vistas son funciones de python

def Home(request):
    return render(request,'index.html')

def Platos(request):

    formulario=FormularioPlatos()
    datosParaTemplate={
        'formularioRegistro':formulario
    }

    #preguntamos si existe alguna conexión de tipo POST
    
    if request.method=='POST':
        #deberíamos capturar los datos del formulario
        datosDelFormulario=FormularioPlatos(request.POST)
        #verificar que si los datos llegaron correctamente(validaciones OK)
        if datosDelFormulario.is_valid():
            #capturamos la información
            datosPlato=datosDelFormulario.cleaned_data
            print(datosPlato)
        
    return render(request,'platos.html',datosParaTemplate)


def Empleados(request):

    formulario=FormularioEmpleados()
    datosParaTemplate={
        'formularioEmpleados':formulario
    }
    if request.method=='POST':
        datosDelFormulario=FormularioEmpleados(request.POST)
        if datosDelFormulario.is_valid():
            datosEmpleado=datosDelFormulario.cleaned_data
            print(datosEmpleado)
    return render(request,'empleados.html',datosParaTemplate)


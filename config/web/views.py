from django.shortcuts import render
from django.shortcuts import redirect


#IMPORTAR EL FORMULARIO A RENDER
from web.formularios.formularioPlatos import FormularioPlatos
from web.formularios.formularioEmpleados import FormularioEmpleados
from web.formularios.formularioEdicionPlatos import FormularioEdicionPlatos
from web.formularios.formularioEdicionEmpleados import FormularioEdicionEmpleados

from web.models import Platos
from web.models import Empleados

# Create your views here.
#las vistas en djangp son los CONTROLADORES

#las vistas son funciones de python

def Home(request):
    return render(request,'index.html')

def MenuPlatos(request):
    platosConsultados=Platos.objects.all()
    
    formulario=FormularioEdicionPlatos()
    
    diccionarioEnvio={
        'platos':platosConsultados,
        'formulario':formulario
    }
    return render(request, 'menuPlatos.html',diccionarioEnvio)

def EditarPlato(request,id):
    if request.method == 'POST':
        datosDelFormulario=FormularioEdicionPlatos(request.POST)
        if datosDelFormulario.is_valid():
            datosPlato=datosDelFormulario.cleaned_data
            try:
                Platos.objects.filter(pk=id).update(precio=datosPlato["precioPlato"])
                print("ÉXITO GUARDANDO DATOS")
            
            except Exception as error:
                print("error", error)

    return redirect('menu')
            
   
def VistaPlatos(request):

    formulario=FormularioPlatos()
    datosParaTemplate={
        'formularioRegistro':formulario,
        'bandera':False
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
            #creamos un objeto de tipo MODELO PLATO
            
            platoNuevo=Platos(
                nombre=datosPlato["nombrePlato"],
                descripcion=datosPlato["descripcionPlato"],
                foto=datosPlato["fotoPlato"],
                precio=datosPlato["precioPlato"],
                tipo=datosPlato["tipoPlato"]
            )
            #Intentamos llevar el objeto platoNuevo
            try:
                platoNuevo.save()
                datosParaTemplate["bandera"]=True
                print("Plato guardado con éxito.")
            except Exception as error:
                datosParaTemplate["bandera"]=False
                print("error: ", error)


    return render(request,'platos.html',datosParaTemplate)


def VistaEmpleados(request):

    formulario=FormularioEmpleados()
    datosParaTemplate={
        'formularioEmpleados':formulario
    }
    if request.method=='POST':
        datosDelFormulario=FormularioEmpleados(request.POST)
        if datosDelFormulario.is_valid():
            datosEmpleado=datosDelFormulario.cleaned_data
            empleadoNuevo=Empleados(
                id = datosEmpleado["idEmpleado"],
                nombres = datosEmpleado["nombresEmpleado"],
                apellidos = datosEmpleado["apellidosEmpleado"],
                foto = datosEmpleado["fotoEmpleado"],
                cargo = datosEmpleado["cargo"],
                salario = datosEmpleado["salario"],
                telefono = datosEmpleado["telefono"]
            )
            try:
                empleadoNuevo.save()
                datosParaTemplate["bandera"]=True
                print("Plato guardado con éxito.")
            except Exception as error:
                datosParaTemplate["bandera"]=False
                print("error: ", error)
    return render(request,'empleados.html',datosParaTemplate)

def ListaEmpleados(request):
    empleadosConsultados=Empleados.objects.all()
    formulario=FormularioEdicionEmpleados()
        
    diccionarioEnvio={
        'empleados':empleadosConsultados,
        'formulario':formulario
    }
    return render(request, 'listaEmpleados.html',diccionarioEnvio)


def EditarEmpleado(request,id):
    if request.method == 'POST':
        datosDelFormulario=FormularioEdicionEmpleados(request.POST)
        if datosDelFormulario.is_valid():
            datosEmpleado=datosDelFormulario.cleaned_data
            try:
                Empleados.objects.filter(pk=id).update(telefono=datosEmpleado["telefono"])
                print("ÉXITO GUARDANDO DATOS")
            
            except Exception as error:
                print("error", error)

    return redirect('listaEmpleados')
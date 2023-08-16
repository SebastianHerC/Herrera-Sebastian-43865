from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import *
from .forms import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    return render(request, "aplicacion/base.html")

@login_required
def profesores(request):
    ctx = {"Profesores": Profesores.objects.all()}
    return render(request, "aplicacion/profesores.html",ctx)
@login_required
def alumnos(request):
    ctx = {"Alumnos": Alumnos.objects.all()}
    return render(request, "aplicacion/alumnos.html",ctx)
@login_required
def sedes(request):
    ctx = {"Sedes": Sedes.objects.all()}
    return render(request, "aplicacion/sedes.html", ctx)
@login_required
def clases(request):
    ctx = {"Clases": Clases.objects.all()}
    return render(request, "aplicacion/clases.html", ctx)


#_________FORMULARIOS_________________
@login_required
def sedesForm(request):
    if request.method == "POST":
        miForm = SedesForm(request.POST)
        print(miForm)
        if miForm.is_valid(): 
            informacion = miForm.cleaned_data
            sede = Sedes(direccion=informacion['direccion'], numeracion=informacion['numeracion'])
            sede.save()
            return render(request, "aplicacion/base.html")
    else:
        miForm = SedesForm()

    return render(request, "aplicacion/sedesForm.html", {"form": miForm})

@login_required
def profesoresForm(request):
    if request.method == "POST":
        miForm = ProfesoresForm(request.POST)
        print(miForm)
        if miForm.is_valid():
            informacion = miForm.cleaned_data
            profe = Profesores(nombre=informacion['nombre'], clase=informacion['clase'])
            profe.save()
            return render(request, "aplicacion/base.html")
    else:
        miForm = ProfesoresForm()

    return render(request, "aplicacion/profesoresForm.html", {"form": miForm})


@login_required
def alumnosForm(request):
    if request.method == "POST":
        miForm = AlumnosForm(request.POST)
        if miForm.is_valid():
            informacion = miForm.cleaned_data
            alumno = Alumnos(nombre=informacion['nombre'], mail=informacion['mail'], edad=informacion['edad'])
            alumno.save()
            return render(request, "aplicacion/base.html")
    else:
        miForm = AlumnosForm()

    return render(request, "aplicacion/alumnosForm.html", {"form": miForm})

@login_required
def clasesForm(request):
    if request.method == "POST":
        miForm = ClasesForm(request.POST)
        if miForm.is_valid():
            informacion = miForm.cleaned_data
            clase = Clases(nombre=informacion['nombre'], dia=informacion['dia'], hora=informacion['hora'], valor=informacion['valor'])
            clase.save()
            return render(request, "aplicacion/base.html")
    else:
        miForm = ClasesForm()

    return render(request, "aplicacion/clasesForm.html", {"form": miForm})



#_______________BUSQUEDAS___________________
@login_required 
def buscarSede(request):
    return render(request, 'aplicacion/buscarSede.html')
@login_required 
def buscarSede2(request):
    if 'direccion' in request.GET:
        direccion = request.GET['direccion']
        numeracion = Sedes.objects.filter(direccion__icontains=direccion)
        return render(request, "aplicacion/resultadoSede.html", {"direccion": direccion, "numeracion": numeracion})
    
@login_required    
def buscarAlumnos(request):
    return render(request, 'aplicacion/buscarAlumnos.html')
@login_required
def buscarAlumnos2(request):
    if 'correo' in request.GET:
        correo = request.GET['correo']
        alumnos = Alumnos.objects.filter(mail__icontains=correo)
        return render(request, "aplicacion/resultadoAlumnos.html", {"correo": correo, "alumnos": alumnos})

@login_required
def buscarProfesores(request):
    return render(request, 'aplicacion/buscarProfesores.html')
@login_required
def buscarProfesores2(request):
    if 'clase' in request.GET:
        clase = request.GET['clase']
        profesores = Profesores.objects.filter(clase__icontains=clase)
        return render(request, "aplicacion/resultadoProfesores.html", {"clase": clase, "profesores": profesores})
@login_required
def buscarClases(request):
    return render(request, 'aplicacion/buscarClases.html')
@login_required
def buscarClases2(request):
    if 'dia' in request.GET:
        dia = request.GET['dia']
        clases = Clases.objects.filter(dia__icontains=dia)
        return render(request, "aplicacion/resultadoClases.html", {"dia": dia, "clases": clases})


#__________________UPDATE Y DELETE__________________
@login_required
def updateSede(request, id_Sede):
    sede = Sedes.objects.get(id=id_Sede)
    
    if request.method == "POST":
        miForm = SedesForm(request.POST)
        if miForm.is_valid():
            sede.direccion = miForm.cleaned_data.get('direccion')
            sede.numeracion = miForm.cleaned_data.get('numeracion')
            sede.save()
            return redirect('sedes') 
    else:
        miForm = SedesForm(initial={'direccion': sede.direccion, 'numeracion': sede.numeracion})
        
    return render(request, "aplicacion/sedesform.html", {'form': miForm, 'sede': sede})

@login_required
def eliminarSede(request, id_Sede):
    sede = get_object_or_404(Sedes, id=id_Sede)
    if request.method == "POST":
        sede.delete()
        return redirect('sedes')
    return render(request, "aplicacion/eliminar_sede.html", {'sede': sede})
@login_required
def updateProfesor(request, id_Profesor):
    profesor = get_object_or_404(Profesores, id=id_Profesor)
    
    if request.method == "POST":
        miForm = ProfesoresForm(request.POST)
        if miForm.is_valid():
            profesor.nombre = miForm.cleaned_data.get('nombre')
            profesor.clase = miForm.cleaned_data.get('clase')
            profesor.save()
            return redirect('profesores')
    else:
        miForm = ProfesoresForm(initial={'nombre': profesor.nombre, 'clase': profesor.clase})
        
    return render(request, "aplicacion/profesoresform.html", {'form': miForm, 'profesor': profesor})
@login_required
def eliminarProfesor(request, id_Profesor):
    profesor = get_object_or_404(Profesores, id=id_Profesor)
    
    if request.method == "POST":
        profesor.delete()
        return redirect('profesores')
    
    return render(request, "aplicacion/eliminar_profesor.html", {'profesor': profesor})

@login_required
def updateClase(request, id_Clase):
    clase = get_object_or_404(Clases, id=id_Clase)
    
    if request.method == "POST":
        miForm = ClasesForm(request.POST)
        if miForm.is_valid():
            clase.nombre = miForm.cleaned_data.get('nombre')
            clase.dia = miForm.cleaned_data.get('dia')
            clase.hora = miForm.cleaned_data.get('hora')
            clase.valor = miForm.cleaned_data.get('valor')
            clase.save()
            return redirect('clases') 
    else:
        miForm = ClasesForm(initial={'nombre': clase.nombre, 'dia': clase.dia, 'hora': clase.hora, 'valor': clase.valor})
        
    return render(request, "aplicacion/clasesform.html", {'form': miForm, 'clase': clase})

@login_required
def eliminarClase(request, id_Clase):
    clase = get_object_or_404(Clases, id=id_Clase)
    if request.method == "POST":
        clase.delete()
        return redirect('clases')
    return render(request, "aplicacion/eliminar_clase.html", {'clase': clase})

@login_required
def updateAlumno(request, id_Alumno):
    alumno = get_object_or_404(Alumnos, id=id_Alumno)
    
    if request.method == "POST":
        miForm = AlumnosForm(request.POST)
        if miForm.is_valid():
            alumno.nombre = miForm.cleaned_data.get('nombre')
            alumno.mail = miForm.cleaned_data.get('mail')
            alumno.edad = miForm.cleaned_data.get('edad')
            alumno.save()
            return redirect('alumnos')  # Redirigir a la vista de lista de alumnos
    else:
        miForm = AlumnosForm(initial={'nombre': alumno.nombre, 'mail': alumno.mail, 'edad': alumno.edad})
        
    return render(request, "aplicacion/alumnosform.html", {'form': miForm, 'alumno': alumno})

@login_required
def eliminarAlumno(request, id_Alumno):
    alumno = get_object_or_404(Alumnos, id=id_Alumno)
    if request.method == "POST":
        alumno.delete()
        return redirect('alumnos')
    return render(request, "aplicacion/eliminar_alumno.html", {'alumno': alumno})

from django.shortcuts import render, get_object_or_404
from .models import Sedes, Profesores, Alumnos, Clases

#_____________DETALE DE UNA FILA________________
@login_required
def detalleSede(request, id_Sede):
    sede = get_object_or_404(Sedes, id=id_Sede)
    return render(request, "aplicacion/detalle_sede.html", {'sede': sede})

@login_required
def detalleProfesor(request, id_Profesor):
    profesor = get_object_or_404(Profesores, id=id_Profesor)
    return render(request, "aplicacion/detalle_profesor.html", {'profesor': profesor})

@login_required
def detalleAlumno(request, id_Alumno):
    alumno = get_object_or_404(Alumnos, id=id_Alumno)
    return render(request, "aplicacion/detalle_alumno.html", {'alumno': alumno})

@login_required
def detalleClase(request, id_Clase):
    clase = get_object_or_404(Clases, id=id_Clase)
    return render(request, "aplicacion/detalle_clase.html", {'clase': clase})


# LOGIN, LOGOUT, REGISTRO

def login_request(request):
    if request.method == "POST":
        miForm = AuthenticationForm(request, data=request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get('username')
            clave = miForm.cleaned_data.get('password')
            user = authenticate(username=usuario, password=clave)
            if user is not None:
                login(request, user)
               
                try:
                    avatar = Avatar.objects.get(user=request.user.id).imagen.url
                except:
                    avatar = '/media/avatares/default.png'
                finally:
                    request.session['avatar'] = avatar

                return render(request, "aplicacion/base.html", {"mensaje": f"Bienvenido {usuario}"})
            else:
                return render(request, "aplicacion/login.html", {"form":miForm, "mensaje": "Datos Inválidos"})
        else:    
            return render(request, "aplicacion/login.html", {"form":miForm, "mensaje": "Datos Inválidos"})

    miForm = AuthenticationForm()

    return render(request, "aplicacion/login.html", {"form":miForm})    

def register(request):
    if request.method == 'POST':
        form = RegistroUsuariosForm(request.POST)  
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            form.save()
            return render(request, "aplicacion/base.html", {"mensaje":"Usuario Creado"})        
    else:
        form = RegistroUsuariosForm() 

    return render(request, "aplicacion/registro.html", {"form": form})    

#__________________REGISTRO DE USUARIOS

@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == "POST":
        form = UserEditForm(request.POST)
        if form.is_valid():
            usuario.email = form.cleaned_data.get('email')
            usuario.password1 = form.cleaned_data.get('password1')
            usuario.password2 = form.cleaned_data.get('password2')
            usuario.first_name = form.cleaned_data.get('first_name')
            usuario.last_name = form.cleaned_data.get('last_name')
            usuario.save()
            return render(request, "aplicacion/base.html", {'mensaje': f"Usuario {usuario.username} actualizado correctamente"})
        else:
            return render(request, "aplicacion/editarPerfil.html", {'form': form})
    else:
        form = UserEditForm(instance=usuario)
    return render(request, "aplicacion/editarPerfil.html", {'form': form, 'usuario':usuario.username})


@login_required
def agregarAvatar(request):
    if request.method == "POST":
        form = AvatarFormulario(request.POST, request.FILES)
        if form.is_valid():
            u = User.objects.get(username=request.user)
            avatarViejo = Avatar.objects.filter(user=u)
            if len(avatarViejo) > 0:
                avatarViejo[0].delete()

            avatar = Avatar(user=u, imagen=form.cleaned_data['imagen'])
            avatar.save()

            imagen = Avatar.objects.get(user=request.user.id).imagen.url
            request.session['avatar'] = imagen

            return render(request, "aplicacion/base.html")
    else:
        form = AvatarFormulario()
    return render(request, "aplicacion/agregarAvatar.html", {'form': form})

@login_required
def acercademi(request):
    mensaje = "Soy egresado de la carrera de fonoaudiología del año 2015. Debido a diferentes situaciones laborales, es que luego de 7 años ejerciendo mi carrera, decidí tomar un cambio de rumbo con el fin de buscar nuevsa oportunidades. Llegué a python, ya que unos amigos me lo recomendaron para coemnzar. Agradezco esos consejos, ya que es algo que realmente me ha a apasionado y me genera interés el aprenderlo. Agradezco la gran disposición y buenas capacidad para poder enseñar tanto de part de Norman, como de los Tutores (fede en mi caso). Muchas gracias por todo el conocimiento transmitido y la buena disponibilidad que presentaron para respodner las dudas."
    return render(request, "aplicacion/acercademi.html", {'mensaje': mensaje})
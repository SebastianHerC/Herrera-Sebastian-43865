Autor: Sebastián Herrera
Nombre del proyecto: "PY GYM"
Objetivo: Poder brindar servicio para tener registro de clases impartidas, profesores, alumnos y sedes. Además de incluir funciones de busqueda
para cada una de estas BD. Poder realizar CRUD, además de brindar herramientos de gestión de usuarios, como cambio de información de personas o 
cambio de avatar. 


Usuario: admin
contraseña: 12345

__________________________URLS_____________________________________

path('', index, name="base"),

_________________Contienen información de las pestañas que se muestran en navbar__________________
    
    path('profesores', profesores, name="profesores"),
    path('clases', clases, name="clases"),
    path('sedes', sedes, name="sedes"),
    path('alumnos', alumnos, name="alumnos"),


_______________________Formularios para modelos creados______________
   
    path('sedes_form/', sedesForm, name="sedes_form"),
    path('alumnos_form/', alumnosForm, name="alumnos_form"),
    path('profesores_form/', profesoresForm, name="profesores_form"),
    path('clases_form/', clasesForm, name="clases_form"),

 _______________________Búsquedas____________________________________

    path('buscar_sede/', buscarSede, name="buscar_sede"),
    path('buscar_sede2/', buscarSede2, name="buscar_sede2"),

    path('buscar_alumnos/', buscarAlumnos, name="buscar_alumnos"),
    path('buscar_alumnos2/', buscarAlumnos2, name="buscar_alumnos2"),

    path('buscar_profesores/', buscarProfesores, name="buscar_profesores"),
    path('buscar_profesores2/', buscarProfesores2, name="buscar_profesores2"),


______________________________CRUD____________________________
    path('buscar_clases/', buscarClases, name="buscar_clases"),
    path('buscar_clases2/', buscarClases2, name="buscar_clases2"),

    path('update_sede/<int:id_Sede>/', updateSede, name="update_sede"),
    path('eliminar_sede/<int:id_Sede>/', eliminarSede, name="eliminar_sede"),

    path('update_profesor/<int:id_Profesor>/', updateProfesor, name="update_profesor"),
    path('eliminar_profesor/<int:id_Profesor>/', eliminarProfesor, name="eliminar_profesor"),

    path('update_clase/<int:id_Clase>/', updateClase, name="update_clase"),
    path('eliminar_clase/<int:id_Clase>/', eliminarClase, name="eliminar_clase"),

    path('update_alumno/<int:id_Alumno>/', updateAlumno, name="update_alumno"),
    path('eliminar_alumno/<int:id_Alumno>/', eliminarAlumno, name="eliminar_alumno"),

    path('detalle_sede/<int:id_Sede>/', detalleSede, name="detalle_sede"),
    path('detalle_profesor/<int:id_Profesor>/', detalleProfesor, name="detalle_profesor"),
    path('detalle_alumno/<int:id_Alumno>/', detalleAlumno, name="detalle_alumno"),
    path('detalle_clase/<int:id_Clase>/', detalleClase, name="detalle_clase"),


________________________Herramientas de usuario_____________________
    path('login/', login_request, name='login'),
    path('logout/', LogoutView.as_view(template_name="aplicacion/logout.html"), name='logout'),
    path('register/', register, name='register'),

    path('editar_perfil/', editarPerfil, name='editar_perfil'),
    path('agregar_avatar/', agregarAvatar, name="agregar_avatar"),

    path('acercademi/', acercademi, name='acercademi'),


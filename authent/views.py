from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login,logout
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse

# Se define la vista que controlara el inicio de sesion
def login_user(request):
    # El Estado en que se ecuentra, primero dice que inici=ie sesion
    state = "Please log in below..."
    # Se inicializan tanto el  usuario como el password y la redireccion a la pagina a la que se dirigia
    username = password = ''
    nextt=""
    # Si se viene de una pagina que requiere login se obtiene la direccion a la que se dirigia
    if request.GET:
        nextt=request.GET['next']
    #Si el metodo es post se quiere saber las credenciales del usuario
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        #Se verifican las credenciales usando el sistema de autentificacion de Django
        user = authenticate(username=username, password=password)
        if user is not None: #Se verifica que si el usuario existe, en caso contrario cambia el estado a que fallo el login
            if user.is_active:   #Se verifica que si el usuario es activo, si le dice al usuario que hable con el admin
                login(request, user) # Si se cumplieron todas las condiciones anteriores, se iniciar sesion
                state = "You're successfully logged in!"
                if not nextt=="/meds/":
                    return HttpResponseRedirect(nextt)

            else:
                state = "Your account is not active, please contact the site admin."
        else:
            state = "Your username and/or password were incorrect."
            #Manda los datos a la template
    return render_to_response(
        'authent/index.html', {
            'state': state,
            'username': username,
            'next':nextt,
            }, RequestContext(request))
# En caso de logout
def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/login/')

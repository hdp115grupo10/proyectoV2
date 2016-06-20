from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login,logout
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse


def login_user(request):
    state = "Please log in below..."

    username = password = ''
    nextt=""
    if request.GET:
        nextt=request.GET['next']

    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                state = "You're successfully logged in!"
                if not nextt=="":
                    return HttpResponseRedirect(nextt)

            else:
                state = "Your account is not active, please contact the site admin."
        else:
            state = "Your username and/or password were incorrect."

    return render_to_response(
        'authent/index.html', {
            'state': state,
            'username': username,
            'next':nextt,
            }, RequestContext(request))

def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/login/')

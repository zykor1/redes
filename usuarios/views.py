#encoding:utf-8
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext #se agrega para poder utilizar la ruta de los archivos estatic se debe poner en todas las funciones
from django.shortcuts import redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from forms import SignupForm
from django.contrib.auth.models import User


def  index(request):
	return render_to_response('index.html',  context_instance=RequestContext(request))

@login_required(login_url='/')
def  logeado(request):
	if request.user.social_auth.filter(provider='twitter').count() > 0:
		getImg = request.user.social_auth.get(provider='twitter').extra_data['profile_image_url']
		return render_to_response('logeado.html', {'imagen': getImg }, context_instance=RequestContext(request))
	return render_to_response('logeado.html',  context_instance=RequestContext(request))


@login_required(login_url='/')
def cerrar(request):
	logout(request)
	return HttpResponseRedirect('/')


def nuevoUserView(request):
	if request.user.is_authenticated() and not request.user.is_staff:
		return redirect('/')
	else:
		if request.method == 'POST':
			formulario = SignupForm(request.POST)
			if formulario.is_valid():
				username = formulario.cleaned_data['username']
				password = formulario.cleaned_data['password']
				email = formulario.cleaned_data['email']
				new_user = User.objects.create_user(username, email ,password)
				new_user.is_active=True
				new_user.is_staff=False
				new_user.is_superuser=False
				new_user.first_name=formulario.cleaned_data['first_name']
				new_user.save()
				return HttpResponseRedirect('/')
		else:
			mensaje ="Los datos no son validos"
			formulario =SignupForm()
		return render_to_response('usuarios/registro.html',{'formulario': formulario }, \
				context_instance=RequestContext(request))


def login(request):
	if request.user.is_authenticated():
		return redirect('/')
	else:
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return redirect('/')
			else:
				return render_to_response('usuarios/login.html', \
					context_instance=RequestContext(request))
		else:
			return render_to_response('usuarios/login.html', \
				context_instance=RequestContext(request))

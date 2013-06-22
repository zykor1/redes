# -*- coding: utf-8 *-*
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
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

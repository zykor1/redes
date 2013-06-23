from django.conf.urls import patterns, include, url
from django.conf import settings
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	 url(r'', include('social_auth.urls')),
    # Examples:
    url(r'^$', 'usuarios.views.index', name='home'),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'usuarios/login.html'}),
    url(r'^logeado/$', 'usuarios.views.logeado', name='Logeado'),
    url(r'^cerrar/$', 'usuarios.views.cerrar'),
    url(r'^registro/$', 'usuarios.views.nuevoUserView'), # agregar nuevo usuario
    # url(r'^redeSociales/', include('redeSociales.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)


# Esta linea hace que en modo produccion o trabajando con el wsgi funcionen
# los static files
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()
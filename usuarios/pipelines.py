from django.conf import settings
from django.utils.http import urlquote
from requests import request, HTTPError
from django.core.files.base import ContentFile
from mongodb.mongodb import MongoDB
import requests


# guardamos en mongo, usuamos upser para insertar en caso de que no exista
# el usuario y en caso de que exista solo lo actualizamos, se valida por medio
# del id de usuario que envia google, upser se encuentra dentro de
# mongodb/mongodb.upser
def guardar_mongo(backend, details, response, social_user, uid,\
                  user, *args, **kwargs):
    if backend.name == "google-oauth2":
        try:
            cliente_mongodb = MongoDB(host='mongodb://%s:%s@%s/%s' % (settings.MONGO_USER, urlquote(settings.MONGO_PWD), settings.MONGO_HOST, settings.MONGO_DB))
            cliente_mongodb.collection = cliente_mongodb[settings.MONGO_DB].google_data
            response['user_django_id'] = user.id
            cliente_mongodb.upser(response['id'], response)
            if user.first_name == "":
                user.first_name = response['given_name']
                user.last_name = response['family_name']
                user.save()
        except Exception, e:
            print e
            status_code = 500

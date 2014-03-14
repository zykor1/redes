from pymongo.errors import AutoReconnect

class MongoDB(object):
  def __init__(self, *args, **kwargs):
    if 'host' in kwargs and not kwargs['host']:
      kwargs.pop('host')
    if 'port' in kwargs and not kwargs['port']:
      kwargs.pop('port')

    self.cliente = None
    #self.mongodb = None
    self._collection = None
    self.conectar(*args, **kwargs)

  def __getitem__(self, index): # obtiene db
    try:
      return self.cliente[index]
    except AutoReconnect:
      return self[index]

  def conectar(self, *args, **kwargs):
    from pymongo import MongoClient
    #from pymongo.errors import ConnectionFailure
    self.cliente = MongoClient(*args, **kwargs) # raise ConnectionFailure

  #def obtener_bd_actual(self):
    #return self.mongodb

  #def establecer_bd_actual(self, mongodb):
    #self.mongodb = mongodb

  #mongodb = property(obtener_bd_actual, establecer_bd_actual)
#
  def obtener_collection(self):
    return self._collection

  def establecer_collection(self, collection):
    self._collection = collection

  collection = property(obtener_collection, establecer_collection)

  def insertar(self, value):
    try:
      return self.collection.insert(value)
    except AutoReconnect:
      return self.insertar(value)

  def upser(self, id, values):
    self.collection.update({'id':id}, values, True)

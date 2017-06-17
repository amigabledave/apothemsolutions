from google.appengine.ext import ndb

#--- datastore classes ----------


class Usuario(ndb.Model):

	#login details
	email = ndb.StringProperty(required=True)
	password_hash = ndb.StringProperty(required=True)

	#user details	
	first_name = ndb.StringProperty(required=True)
	last_name = ndb.StringProperty(required=True)
	client = ndb.StringProperty()
	is_admin = ndb.BooleanProperty(default=False)

	
	#tracker fields
	created = ndb.DateTimeProperty(auto_now_add=True)	
	last_modified = ndb.DateTimeProperty(auto_now=True)
	created_by = ndb.KeyProperty()


	@classmethod # This means you can call a method directly on the Class (no on a Class Instance)
	def get_by_usuario_id(cls, usuario_id):
		return Usuario.get_by_id(usuario_id)

	@classmethod
	def get_by_email(cls, email):
		return Usuario.query(Usuario.email == email).get()

	@classmethod
	def valid_login(cls, email, password):
		usuario = cls.get_by_email(email)
		if usuario and validate_password(email, password, usuario.password_hash):
			return usuario


class TablaCNBV(ndb.Model):
	created = ndb.DateTimeProperty(auto_now_add=True)
	nombre = ndb.StringProperty(required=True)
	descripcion = ndb.StringProperty(required=True)
	url_fuente = ndb.StringProperty()
	unidades = ndb.JsonProperty()
	registros = ndb.IntegerProperty(default=0)
	diccionarios = ndb.JsonProperty()


class CsvCNBV(ndb.Model):
	created = ndb.DateTimeProperty(auto_now_add=True)
	blob_key = ndb.BlobKeyProperty(required=True)
	Key_TablaCNBV = ndb.KeyProperty(kind=TablaCNBV, required=True)	
	nombre_tablaCNBV =  ndb.StringProperty(required=True)
	nombre = ndb.StringProperty()
	covertura = ndb.JsonProperty()
	rows_transfered = ndb.IntegerProperty(default=0)


class Slide(ndb.Model):	
	created = ndb.DateTimeProperty(auto_now_add=True)	
	lead = ndb.StringProperty()
	pic_key = ndb.BlobKeyProperty()
	pic_url = ndb.StringProperty()
	number = ndb.IntegerProperty(required=True, default=0)	
	tags = ndb.JsonProperty()
	doc_name = ndb.StringProperty()
	is_private = ndb.BooleanProperty(default=False)
	client = ndb.StringProperty()
	

class DatoCNBV(ndb.Model):
	
	created = ndb.DateTimeProperty(auto_now_add=True)
	tabla = ndb.KeyProperty(kind=TablaCNBV, required=True)	
	archivo_fuente = ndb.KeyProperty(kind=CsvCNBV, required=True)
		
	periodo = ndb.IntegerProperty()
	institucion = ndb.StringProperty()
	tec = ndb.StringProperty()
	estado = ndb.StringProperty()	
	cliente = ndb.StringProperty()
	moneda = ndb.StringProperty()
	intervalo = ndb.StringProperty() #Se refiere al rango del plazo
	monto = ndb.StringProperty() #Se refiere al rango del monto
	destino = ndb.StringProperty()
	garantia = ndb.StringProperty()
	calificacion = ndb.StringProperty()
	sector = ndb.StringProperty()

	#Formato vertical
	tipo_valor = ndb.StringProperty()
	valor = ndb.FloatProperty()
	
	#Formato horizontal
	saldo_total = ndb.FloatProperty()
	creditos = ndb.FloatProperty()
	acreditados = ndb.FloatProperty()
	tasa = ndb.FloatProperty()
	plazo = ndb.FloatProperty() #Plazo ponderado del remanente
	vigencia = ndb.FloatProperty() #Plazo  original
	imor = ndb.FloatProperty()

	saldo_acum = ndb.FloatProperty()
	porc_acum = ndb.FloatProperty()



#--- Validation and security functions ----------
import hashlib, random
secret = 'echeverriaesputo'

def make_secure_val(val):
    return '%s|%s' % (val, hashlib.sha256(secret + val).hexdigest())

def check_secure_val(secure_val):
	val = secure_val.split('|')[0]
	if secure_val == make_secure_val(val):
		return val

def make_salt(lenght = 5):
    return ''.join(random.choice(string.letters) for x in range(lenght))

def make_password_hash(email, password, salt = None):
	if not salt:
		salt = make_salt()
	h = hashlib.sha256(email + password + salt).hexdigest()
	return '%s|%s' % (h, salt)

def validate_password(email, password, h):
	salt = h.split('|')[1]
	return h == make_password_hash(email, password, salt)


	
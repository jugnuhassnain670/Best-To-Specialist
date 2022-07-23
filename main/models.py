from django.db import models

class Contact(models.Model):
	Name=models.CharField(max_length=200)
	Email=models.EmailField()
	Message=models.TextField()
	Subject=models.TextField()
	"""docstring for Contact"""
	def __str__(self):
		return self.Name


class Registration(models.Model):
	Name=models.CharField(max_length=200)
	Skills=models.CharField(max_length=200)
	Phoneno=models.CharField(max_length=13)
	Email=models.EmailField()
	Message=models.TextField()
	"""docstring for Registration"""
	def __str__(self):
		return self.Name


#Services
class Ambulanceserviceinlahore(models.Model):
	Name=models.CharField(max_length=200)
	Email=models.EmailField()
	Phoneno=models.TextField()
	Message=models.TextField()
	"""docstring for Ambulanceserviceinlahore"""
	def __str__(self):
		return self.Name

class Acservice(models.Model):
	Name=models.CharField(max_length=200)
	Email=models.EmailField()
	Phoneno=models.TextField()
	Message=models.TextField()
	"""docstring for Acservice"""
	def __str__(self):
		return self.Name

class Actechnicianservice(models.Model):
	Name=models.CharField(max_length=200)
	Email=models.EmailField()
	Phoneno=models.TextField()
	Message=models.TextField()
	"""docstring for Actechnicianservice"""
	def __str__(self):
		return self.Name


class Carpenteryservice(models.Model):
	Name=models.CharField(max_length=200)
	Email=models.EmailField()
	Phoneno=models.TextField()
	Message=models.TextField()
	"""docstring for Carpenteryservice"""
	def __str__(self):
		return self.Name

class Electricalservice(models.Model):
	Name=models.CharField(max_length=200)
	Email=models.EmailField()
	Phoneno=models.TextField()
	Message=models.TextField()
	"""docstring for Electricalservice"""
	def __str__(self):
		return self.Name


class Gardeningservice(models.Model):
	Name=models.CharField(max_length=200)
	Email=models.EmailField()
	Phoneno=models.TextField()
	Message=models.TextField()
	"""docstring for Gardeningservice"""
	def __str__(self):
		return self.Name


class Generatorservice(models.Model):
	Name=models.CharField(max_length=200)
	Email=models.EmailField()
	Phoneno=models.TextField()
	Message=models.TextField()
	"""docstring for Generatorservice"""
	def __str__(self):
		return self.Name

class Plumbingservice(models.Model):
	Name=models.CharField(max_length=200)
	Email=models.EmailField()
	Phoneno=models.TextField()
	Message=models.TextField()
	"""docstring for Plumbingservice"""
	def __str__(self):
		return self.Name

class Paintservice(models.Model):
	Name=models.CharField(max_length=200)
	Email=models.EmailField()
	Phoneno=models.TextField()
	Message=models.TextField()
	"""docstring for Paintservice"""
	def __str__(self):
		return self.Name


class Plantservice(models.Model):
	Name=models.CharField(max_length=200)
	Email=models.EmailField()
	Phoneno=models.TextField()
	Message=models.TextField()
	"""docstring for Plantservice"""
	def __str__(self):
		return self.Name


class Masonservice(models.Model):
	Name=models.CharField(max_length=200)
	Email=models.EmailField()
	Phoneno=models.TextField()
	Message=models.TextField()
	"""docstring for Masonservice"""
	def __str__(self):
		return self.Name


#premium
class Heatproofing(models.Model):
	Name=models.CharField(max_length=200)
	Email=models.EmailField()
	Phoneno=models.TextField()
	Message=models.TextField()
	"""docstring for Heatproofing"""
	def __str__(self):
		return self.Name

class Waterproofing(models.Model):
	Name=models.CharField(max_length=200)
	Email=models.EmailField()
	Phoneno=models.TextField()
	Message=models.TextField()
	"""docstring for Waterproofing"""
	def __str__(self):
		return self.Name

class Depoxyflooring(models.Model):
	Name=models.CharField(max_length=200)
	Email=models.EmailField()
	Phoneno=models.TextField()
	Message=models.TextField()
	"""docstring for Depoxyflooring"""
	def __str__(self):
		return self.Name

class Epoxyflooring(models.Model):
	Name=models.CharField(max_length=200)
	Email=models.EmailField()
	Phoneno=models.TextField()
	Message=models.TextField()
	"""docstring for Epoxyflooring"""
	def __str__(self):
		return self.Name

class Falseceiling(models.Model):
	Name=models.CharField(max_length=200)
	Email=models.EmailField()
	Phoneno=models.TextField()
	Message=models.TextField()
	"""docstring for Falseceiling"""
	def __str__(self):
		return self.Name

class Graphiccoating(models.Model):
	Name=models.CharField(max_length=200)
	Email=models.EmailField()
	Phoneno=models.TextField()
	Message=models.TextField()
	"""docstring for Graphiccoating"""
	def __str__(self):
		return self.Name

class Exteriorninterior(models.Model):
	Name=models.CharField(max_length=200)
	Email=models.EmailField()
	Phoneno=models.TextField()
	Message=models.TextField()
	"""docstring for Exteriorninterior"""
	def __str__(self):
		return self.Name


#addon
class Carpetceiling(models.Model):
	Name=models.CharField(max_length=200)
	Email=models.EmailField()
	Phoneno=models.TextField()
	Message=models.TextField()
	"""docstring for Carpetceiling"""
	def __str__(self):
		return self.Name


class Watertankcleaning(models.Model):
	Name=models.CharField(max_length=200)
	Email=models.EmailField()
	Phoneno=models.TextField()
	Message=models.TextField()
	"""docstring for Watertankcleaning"""
	def __str__(self):
		return self.Name

class Surveillancesystem(models.Model):
	Name=models.CharField(max_length=200)
	Email=models.EmailField()
	Phoneno=models.TextField()
	Message=models.TextField()
	"""docstring for Surveillancesystem"""
	def __str__(self):
		return self.Name

class Sofacleaning(models.Model):
	Name=models.CharField(max_length=200)
	Email=models.EmailField()
	Phoneno=models.TextField()
	Message=models.TextField()
	"""docstring for Sofacleaning"""
	def __str__(self):
		return self.Name

class Flooringsolutions(models.Model):
	Name=models.CharField(max_length=200)
	Email=models.EmailField()
	Phoneno=models.TextField()
	Message=models.TextField()
	"""docstring for Flooringsolutions"""
	def __str__(self):
		return self.Name

class Glazingservices(models.Model):
	Name=models.CharField(max_length=200)
	Email=models.EmailField()
	Phoneno=models.TextField()
	Message=models.TextField()
	"""docstring for Glazingservices"""
	def __str__(self):
		return self.Name

class Pabxsystem(models.Model):
	Name=models.CharField(max_length=200)
	Email=models.EmailField()
	Phoneno=models.TextField()
	Message=models.TextField()
	"""docstring for Pabxsystem"""
	def __str__(self):
		return self.Name

class Fumigationservices(models.Model):
	Name=models.CharField(max_length=200)
	Email=models.EmailField()
	Phoneno=models.TextField()
	Message=models.TextField()
	"""docstring for Fumigationservices"""
	def __str__(self):
		return self.Name


#automotive
class Batteryreplacement(models.Model):
	Name=models.CharField(max_length=200)
	Email=models.EmailField()
	Phoneno=models.TextField()
	Message=models.TextField()
	"""docstring for Batteryreplacement"""
	def __str__(self):
		return self.Name

class Brakerepairreplacement(models.Model):
	Name=models.CharField(max_length=200)
	Email=models.EmailField()
	Phoneno=models.TextField()
	Message=models.TextField()
	"""docstring for Brakerepairreplacement"""
	def __str__(self):
		return self.Name

class Cardetailing(models.Model):
	Name=models.CharField(max_length=200)
	Email=models.EmailField()
	Phoneno=models.TextField()
	Message=models.TextField()
	"""docstring for Cardetailing"""
	def __str__(self):
		return self.Name

class Headlightrepair(models.Model):
	Name=models.CharField(max_length=200)
	Email=models.EmailField()
	Phoneno=models.TextField()
	Message=models.TextField()
	"""docstring for Headlightrepair"""
	def __str__(self):
		return self.Name

class Oilchange(models.Model):
	Name=models.CharField(max_length=200)
	Email=models.EmailField()
	Phoneno=models.TextField()
	Message=models.TextField()
	"""docstring for Oilchange"""
	def __str__(self):
		return self.Name

class Carwash(models.Model):
	Name=models.CharField(max_length=200)
	Email=models.EmailField()
	Phoneno=models.TextField()
	Message=models.TextField()
	"""docstring for Carwash"""
	def __str__(self):
		return self.Name

class Glasscoatingservices(models.Model):
	Name=models.CharField(max_length=200)
	Email=models.EmailField()
	Phoneno=models.TextField()
	Message=models.TextField()
	"""docstring for Glasscoatingservices"""
	def __str__(self):
		return self.Name


class SignUp(models.Model):
	Name=models.CharField(max_length=200)
	Email=models.EmailField()
	Phoneno=models.TextField()
	Address=models.TextField()
	Message=models.TextField()
	"""docstring for SignUp"""
	def __str__(self):
		return self.Name






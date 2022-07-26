from django.shortcuts import render,HttpResponse,redirect
from .models import Contact
from .models import Registration

# services models 
from .models import Ambulanceserviceinlahore
from .models import Acservice
from .models import Actechnicianservice
from .models import Carpenteryservice
from .models import Electricalservice
from .models import Gardeningservice
from .models import Generatorservice
from .models import Plumbingservice
from .models import Paintservice
from .models import Plantservice
from .models import Masonservice


#premium
from .models import Heatproofing
from .models import Waterproofing
from .models import Depoxyflooring
from .models import Epoxyflooring
from .models import Falseceiling
from .models import Graphiccoating
from .models import Exteriorninterior


#addon
from .models import Carpetceiling
from .models import Watertankcleaning
from .models import Surveillancesystem
from .models import Sofacleaning
from .models import Flooringsolutions
from .models import Glazingservices
from .models import Pabxsystem
from .models import Fumigationservices

#automotive
from .models import Batteryreplacement
from .models import Brakerepairreplacement
from .models import Cardetailing
from .models import Headlightrepair
from .models import Oilchange
from .models import Carwash
from .models import Glasscoatingservices


from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import CreateUserForm

def registerPage(request):
	if request.user.is_authenticated:
		return redirect('index')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('login')
			

		context = {'form':form}
		return render(request, 'registration.html', context)

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('index')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('index')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')

# @login_required(login_url='login')
def index(request):
    if request.method == "POST":
        contact=Contact()
        Name=request.POST.get('Name')
        Email=request.POST.get('Email')
        Subject=request.POST.get('Subject')
        Message=request.POST.get('Message')
        contact.Name=Name
        contact.Email=Email
        contact.Subject=Subject
        contact.Message=Message
        contact.save()
    return render(request, 'index.html')
		




def ambulanceserviceinlahore(request):
	if request.method == "POST":
		ambulanceserviceinlahore=Ambulanceserviceinlahore()
		Name=request.POST.get('Name')
		Email=request.POST.get('Email')
		Phoneno=request.POST.get('Phoneno')
		Message=request.POST.get('Message')
		ambulanceserviceinlahore.Name=Name
		ambulanceserviceinlahore.Email=Email
		ambulanceserviceinlahore.Phoneno=Phoneno
		ambulanceserviceinlahore.Message=Message
		ambulanceserviceinlahore.save()
	return render(request,'ambulanceserviceinlahore.html')





def acservice(request):
	if request.method == "POST":
		acservice=Acservice()
		Name=request.POST.get('Name')
		Email=request.POST.get('Email')
		Phoneno=request.POST.get('Phoneno')
		Message=request.POST.get('Message')
		acservice.Name=Name
		acservice.Email=Email
		acservice.Phoneno=Phoneno
		acservice.Message=Message
		acservice.save()
	return render(request,'acservice.html')




def actechnicianservice(request):
	if request.method == "POST":
		actechnicianservice=Actechnicianservice()
		Name=request.POST.get('Name')
		Email=request.POST.get('Email')
		Phoneno=request.POST.get('Phoneno')
		Message=request.POST.get('Message')
		actechnicianservice.Name=Name
		actechnicianservice.Email=Email
		actechnicianservice.Phoneno=Phoneno
		actechnicianservice.Message=Message
		actechnicianservice.save()
	return render(request,'actechnicianservice.html')

def carpenteryservice(request):
	if request.method == "POST":
		carpenteryservice=Carpenteryservice()
		Name=request.POST.get('Name')
		Email=request.POST.get('Email')
		Phoneno=request.POST.get('Phoneno')
		Message=request.POST.get('Message')
		carpenteryservice.Name=Name
		carpenteryservice.Email=Email
		carpenteryservice.Phoneno=Phoneno
		carpenteryservice.Message=Message
		carpenteryservice.save()
	return render(request,'carpenteryservice.html')

def electricalservice(request):
	if request.method == "POST":
		electricalservice=Electricalservice()
		Name=request.POST.get('Name')
		Email=request.POST.get('Email')
		Phoneno=request.POST.get('Phoneno')
		Message=request.POST.get('Message')
		electricalservice.Name=Name
		electricalservice.Email=Email
		electricalservice.Phoneno=Phoneno
		electricalservice.Message=Message
		electricalservice.save()
	return render(request,'electricalservice.html')

def gardeningservice(request):
	if request.method == "POST":
		gardeningservice=Gardeningservice()
		Name=request.POST.get('Name')
		Email=request.POST.get('Email')
		Phoneno=request.POST.get('Phoneno')
		Message=request.POST.get('Message')
		gardeningservice.Name=Name
		gardeningservice.Email=Email
		gardeningservice.Phoneno=Phoneno
		gardeningservice.Message=Message
		gardeningservice.save()
	return render(request,'gardeningservice.html') 

def generatorservice(request):
	if request.method == "POST":
		generatorservice=Generatorservice()
		Name=request.POST.get('Name')
		Email=request.POST.get('Email')
		Phoneno=request.POST.get('Phoneno')
		Message=request.POST.get('Message')
		generatorservice.Name=Name
		generatorservice.Email=Email
		generatorservice.Phoneno=Phoneno
		generatorservice.Message=Message
		generatorservice.save()
	return render(request,'generatorservice.html') 

def plumbingservice(request):
	if request.method == "POST":
		plumbingservice=Plumbingservice()
		Name=request.POST.get('Name')
		Email=request.POST.get('Email')
		Phoneno=request.POST.get('Phoneno')
		Message=request.POST.get('Message')
		plumbingservice.Name=Name
		plumbingservice.Email=Email
		plumbingservice.Phoneno=Phoneno
		plumbingservice.Message=Message
		plumbingservice.save()
	return render(request,'plumbingservice.html') 

def plantservice(request):
	if request.method == "POST":
		plantservice=Plantservice()
		Name=request.POST.get('Name')
		Email=request.POST.get('Email')
		Phoneno=request.POST.get('Phoneno')
		Message=request.POST.get('Message')
		plantservice.Name=Name
		plantservice.Email=Email
		plantservice.Phoneno=Phoneno
		plantservice.Message=Message
		plantservice.save()
	return render(request,'plantservice.html')

def paintservice(request):
	if request.method == "POST":
		paintservice=Paintservice()
		Name=request.POST.get('Name')
		Email=request.POST.get('Email')
		Phoneno=request.POST.get('Phoneno')
		Message=request.POST.get('Message')
		paintservice.Name=Name
		paintservice.Email=Email
		paintservice.Phoneno=Phoneno
		paintservice.Message=Message
		paintservice.save()
	return render(request,'paintservice.html') 

def masonservice(request):
	if request.method == "POST":
		masonservice=Masonservice()
		Name=request.POST.get('Name')
		Email=request.POST.get('Email')
		Phoneno=request.POST.get('Phoneno')
		Message=request.POST.get('Message')
		masonservice.Name=Name
		masonservice.Email=Email
		masonservice.Phoneno=Phoneno
		masonservice.Message=Message
		masonservice.save()
	return render(request,'masonservice.html')






#premium services start
def heatproofing(request):
	if request.method == "POST":
		heatproofing=Heatproofing()
		Name=request.POST.get('Name')
		Email=request.POST.get('Email')
		Phoneno=request.POST.get('Phoneno')
		Message=request.POST.get('Message')
		heatproofing.Name=Name
		heatproofing.Email=Email
		heatproofing.Phoneno=Phoneno
		heatproofing.Message=Message
		heatproofing.save()
	return render(request,'heatproofing.html')

def waterproofing(request):
	if request.method == "POST":
		waterproofing=Waterproofing()
		Name=request.POST.get('Name')
		Email=request.POST.get('Email')
		Phoneno=request.POST.get('Phoneno')
		Message=request.POST.get('Message')
		waterproofing.Name=Name
		waterproofing.Email=Email
		waterproofing.Phoneno=Phoneno
		waterproofing.Message=Message
		waterproofing.save()
	return render(request,'waterproofing.html') \


def depoxyflooring(request):
	if request.method == "POST":
		depoxyflooring=Depoxyflooring()
		Name=request.POST.get('Name')
		Email=request.POST.get('Email')
		Phoneno=request.POST.get('Phoneno')
		Message=request.POST.get('Message')
		depoxyflooring.Name=Name
		depoxyflooring.Email=Email
		depoxyflooring.Phoneno=Phoneno
		depoxyflooring.Message=Message
		depoxyflooring.save()
	return render(request,'depoxyflooring.html') 

def epoxyflooring(request):
	if request.method == "POST":
		epoxyflooring=Epoxyflooring()
		Name=request.POST.get('Name')
		Email=request.POST.get('Email')
		Phoneno=request.POST.get('Phoneno')
		Message=request.POST.get('Message')
		epoxyflooring.Name=Name
		epoxyflooring.Email=Email
		epoxyflooring.Phoneno=Phoneno
		epoxyflooring.Message=Message
		epoxyflooring.save()
	return render(request,'epoxyflooring.html') 


def falseceiling(request):
	if request.method == "POST":
		falseceiling=Falseceiling()
		Name=request.POST.get('Name')
		Email=request.POST.get('Email')
		Phoneno=request.POST.get('Phoneno')
		Message=request.POST.get('Message')
		falseceiling.Name=Name
		falseceiling.Email=Email
		falseceiling.Phoneno=Phoneno
		falseceiling.Message=Message
		falseceiling.save()
	return render(request,'falseceiling.html') 

def graphiccoating(request):
	if request.method == "POST":
		graphiccoating=Graphiccoating()
		Name=request.POST.get('Name')
		Email=request.POST.get('Email')
		Phoneno=request.POST.get('Phoneno')
		Message=request.POST.get('Message')
		graphiccoating.Name=Name
		graphiccoating.Email=Email
		graphiccoating.Phoneno=Phoneno
		graphiccoating.Message=Message
		graphiccoating.save()
	return render(request,'graphiccoating.html') 

def exteriorninterior(request):
	if request.method == "POST":
		exteriorninterior=Exteriorninterior()
		Name=request.POST.get('Name')
		Email=request.POST.get('Email')
		Phoneno=request.POST.get('Phoneno')
		Message=request.POST.get('Message')
		exteriorninterior.Name=Name
		exteriorninterior.Email=Email
		exteriorninterior.Phoneno=Phoneno
		exteriorninterior.Message=Message
		exteriorninterior.save()
	return render(request,'exteriorninterior.html') 


#premium services end


#Addon services Start
def carpetceiling(request):
	if request.method == "POST":
		carpetceiling=Carpetceiling()
		Name=request.POST.get('Name')
		Email=request.POST.get('Email')
		Phoneno=request.POST.get('Phoneno')
		Message=request.POST.get('Message')
		carpetceiling.Name=Name
		carpetceiling.Email=Email
		carpetceiling.Phoneno=Phoneno
		carpetceiling.Message=Message
		carpetceiling.save()
	return render(request,'carpetceiling.html') 

def watertankcleaning(request):
	if request.method == "POST":
		watertankcleaning=Watertankcleaning()
		Name=request.POST.get('Name')
		Email=request.POST.get('Email')
		Phoneno=request.POST.get('Phoneno')
		Message=request.POST.get('Message')
		watertankcleaning.Name=Name
		watertankcleaning.Email=Email
		watertankcleaning.Phoneno=Phoneno
		watertankcleaning.Message=Message
		watertankcleaning.save()
	return render(request,'watertankcleaning.html') 

def surveillancesystem(request):
	if request.method == "POST":
		surveillancesystem=Surveillancesystem()
		Name=request.POST.get('Name')
		Email=request.POST.get('Email')
		Phoneno=request.POST.get('Phoneno')
		Message=request.POST.get('Message')
		surveillancesystem.Name=Name
		surveillancesystem.Email=Email
		surveillancesystem.Phoneno=Phoneno
		surveillancesystem.Message=Message
		surveillancesystem.save()
	return render(request,'surveillancesystem.html') 

def sofacleaning(request):
	if request.method == "POST":
		sofacleaning=Sofacleaning()
		Name=request.POST.get('Name')
		Email=request.POST.get('Email')
		Phoneno=request.POST.get('Phoneno')
		Message=request.POST.get('Message')
		sofacleaning.Name=Name
		sofacleaning.Email=Email
		sofacleaning.Phoneno=Phoneno
		sofacleaning.Message=Message
		sofacleaning.save()
	return render(request,'sofacleaning.html') 

def flooringsolutions(request):
	if request.method == "POST":
		flooringsolutions=Flooringsolutions()
		Name=request.POST.get('Name')
		Email=request.POST.get('Email')
		Phoneno=request.POST.get('Phoneno')
		Message=request.POST.get('Message')
		flooringsolutions.Name=Name
		flooringsolutions.Email=Email
		flooringsolutions.Phoneno=Phoneno
		flooringsolutions.Message=Message
		flooringsolutions.save()
	return render(request,'flooringsolutions.html')


def glazingservices(request):
	if request.method == "POST":
		glazingservices=Glazingservices()
		Name=request.POST.get('Name')
		Email=request.POST.get('Email')
		Phoneno=request.POST.get('Phoneno')
		Message=request.POST.get('Message')
		glazingservices.Name=Name
		glazingservices.Email=Email
		glazingservices.Phoneno=Phoneno
		glazingservices.Message=Message
		glazingservices.save()
	return render(request,'glazingservices.html') 

def pabxsystem(request):
	if request.method == "POST":
		pabxsystem=Pabxsystem()
		Name=request.POST.get('Name')
		Email=request.POST.get('Email')
		Phoneno=request.POST.get('Phoneno')
		Message=request.POST.get('Message')
		pabxsystem.Name=Name
		pabxsystem.Email=Email
		pabxsystem.Phoneno=Phoneno
		pabxsystem.Message=Message
		pabxsystem.save()
	return render(request,'pabxsystem.html') 

def fumigationservices(request):
	if request.method == "POST":
		fumigationservices=Fumigationservices()
		Name=request.POST.get('Name')
		Email=request.POST.get('Email')
		Phoneno=request.POST.get('Phoneno')
		Message=request.POST.get('Message')
		fumigationservices.Name=Name
		fumigationservices.Email=Email
		fumigationservices.Phoneno=Phoneno
		fumigationservices.Message=Message
		fumigationservices.save()
	return render(request,'fumigationservices.html') 

#Addon services end
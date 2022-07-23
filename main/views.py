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
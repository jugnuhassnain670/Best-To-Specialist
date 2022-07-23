from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registration/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    
    path('ambulanceserviceinlahore/', views.ambulanceserviceinlahore, name='ambulanceserviceinlahore'),
    path('acservice/', views.acservice, name='acservice'),
    path('actechnicianservice/', views.actechnicianservice, name='actechnicianservice'),
    path('carpenteryservice/', views.carpenteryservice, name='carpenteryservice'),
    path('electricalservice/', views.electricalservice, name='electricalservice'),
    path('gardeningservice/', views.gardeningservice, name='gardeningservice'),
    path('generatorservice/', views.generatorservice, name='generatorservice'),
    path('plumbingservice/', views.plumbingservice, name='plumbingservice'),
    path('paintservice/', views.paintservice, name='paintservice'),
    # End of services 
    
]

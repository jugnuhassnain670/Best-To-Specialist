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
    
    #premium services start
    path('heatproofing/', views.heatproofing, name='heatproofing'),
    path('waterproofing/', views.waterproofing, name='waterproofing'),
    path('depoxyflooring/', views.depoxyflooring, name='depoxyflooring'),
    path('epoxyflooring/', views.epoxyflooring, name='epoxyflooring'),
    path('falseceiling/', views.falseceiling, name='falseceiling'),
    path('graphiccoating/', views.graphiccoating, name='graphiccoating'),
    path('exteriorninterior/', views.exteriorninterior, name='exteriorninterior'),
    #premium services end
    
    #Addon service start
    path('carpetceiling/', views.carpetceiling, name='carpetceiling'),
    path('watertankcleaning/', views.watertankcleaning, name='watertankcleaning'),
    path('surveillancesystem/', views.surveillancesystem, name='surveillancesystem'),
    path('sofacleaning/', views.sofacleaning, name='sofacleaning'),
    path('flooringsolutions/', views.flooringsolutions, name='flooringsolutions'),
    path('glazingservices/', views.glazingservices, name='glazingservices'),
    path('pabxsystem/', views.pabxsystem, name='pabxsystem'),
    path('fumigationservices/', views.fumigationservices, name='fumigationservices'),
    #Addon service end
    
]

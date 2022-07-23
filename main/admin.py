from django.contrib import admin


from .models import Contact
from .models import Registration

#service
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
from .models import SignUp

# Register your models here.

admin.site.register(Contact)
admin.site.register(Registration)
admin.site.register(SignUp)

#service
admin.site.register(Ambulanceserviceinlahore)
admin.site.register(Acservice)
admin.site.register(Actechnicianservice)
admin.site.register(Carpenteryservice)
admin.site.register(Electricalservice)
admin.site.register(Gardeningservice)
admin.site.register(Generatorservice)
admin.site.register(Plumbingservice)
admin.site.register(Paintservice)
admin.site.register(Plantservice)
admin.site.register(Masonservice)

#premium
admin.site.register(Heatproofing)
admin.site.register(Waterproofing)
admin.site.register(Depoxyflooring)
admin.site.register(Epoxyflooring)
admin.site.register(Falseceiling)
admin.site.register(Graphiccoating)
admin.site.register(Exteriorninterior)

#addon
admin.site.register(Carpetceiling)
admin.site.register(Watertankcleaning)
admin.site.register(Surveillancesystem)
admin.site.register(Sofacleaning)
admin.site.register(Flooringsolutions)
admin.site.register(Glazingservices)
admin.site.register(Pabxsystem)
admin.site.register(Fumigationservices)

#automotive
admin.site.register(Batteryreplacement)
admin.site.register(Brakerepairreplacement)
admin.site.register(Cardetailing)
admin.site.register(Headlightrepair)
admin.site.register(Oilchange)
admin.site.register(Carwash)
admin.site.register(Glasscoatingservices)

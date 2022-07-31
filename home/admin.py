from django.contrib import admin
from home.models import emp_personal 
from home.models import emp_medical 
from home.models import emp_emergency 
from home.models import emp_education 
from home.models import emp_courses 
from home.models import emp_experience 
from home.models import emp_job 
from home.models import Register_Vehicle 
from home.models import route 
from home.models import maintenance 
from home.models import city 
from home.models import routte 
from home.models import stop 



# Register your models here.
admin.site.register(emp_personal)
admin.site.register(emp_medical)
admin.site.register(emp_emergency)
admin.site.register(emp_education)
admin.site.register(emp_courses)
admin.site.register(emp_experience)
admin.site.register(emp_job)
admin.site.register(Register_Vehicle)
admin.site.register(route)
admin.site.register(maintenance)
admin.site.register(city)
admin.site.register(routte)
admin.site.register(stop)
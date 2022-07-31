from multiprocessing import context
from string import Template
from urllib import response
from django import template
from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.http.response import HttpResponseRedirect


# import database
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



def index(request):

    # personal
    if request.method == "POST":
        emp_id=request.POST.get('emp_id')
        name=request.POST.get('name')
        fname=request.POST.get('fname')
        gender=request.POST.get('gender')
        dob=request.POST.get('dob')
        cnic=request.POST.get('cnic')
        ph1=request.POST.get('ph1')
        ph2=request.POST.get('ph2')
        email=request.POST.get('email')
        city=request.POST.get('city')
        adress=request.POST.get('adress')
        postal_code=request.POST.get('postal_code')
        marital_status=request.POST.get('marital_status')
        designation=request.POST.get('designation')
        image=request.FILES.get('image')
        Employee = emp_personal(emp_id=emp_id,name=name , fname =fname , gender=gender , dob=dob , cnic = cnic , ph1 = ph1 ,ph2=ph2,email=email,city=city,adress=adress,postal_code=postal_code,marital_status=marital_status , designation=designation,image=image)
        Employee.save()




        # emergency
        name_emergency=request.POST.get('name_emergency')
        relation_emergency=request.POST.get('relation_emergency')
        adress_emergency=request.POST.get('adress_emergency')
        city_emergency=request.POST.get('city_emergency')
        email_emergency=request.POST.get('email_emergency')
        ph1_emergency=request.POST.get('ph1_emergency')
        ph2_emergency=request.POST.get('ph2_emergency')
        Emp_emergency = emp_emergency(emp_id=emp_id,name=name_emergency , relation =relation_emergency , adress=adress_emergency , city=city_emergency , email=email_emergency , ph1=ph1_emergency , ph2=ph2_emergency )
        Emp_emergency.save()



        # medical
        blood_medical=request.POST.get('blood_medical')
        organ_doner_medical=request.POST.get('organ_doner_medical')
        disability_medical=request.POST.get('disability_medical')
        fitness_medical=request.POST.get('fitness_medical')
        Emp_medical = emp_medical(emp_id=emp_id,blood=blood_medical , organ_doner =organ_doner_medical , disability=disability_medical , fitness=fitness_medical )
        Emp_medical.save()


        # courses
        title_courses=request.POST.get('title_courses')
        institute_courses=request.POST.get('institute_courses')
        Duration_courses=request.POST.get('Duration_courses')
        date_of_complition_courses=request.POST.get('date_of_complition_courses')
        certificate_courses=request.POST.get('certificate_courses')
        no_of_project_courses=request.POST.get('no_of_project_courses')
        Emp_courses = emp_courses(emp_id=emp_id,title=title_courses , institute =institute_courses , Duration=Duration_courses , date_of_complition=date_of_complition_courses ,certificate=certificate_courses , no_of_project=no_of_project_courses )
        Emp_courses.save()



        # job details
        Designation_job=request.POST.get('Designation_job')
        job_description_job=request.POST.get('job_description_job')
        duty_time_job=request.POST.get('duty_time_job')
        Emp_job = emp_job(emp_id=emp_id,Designation=Designation_job , job_description =job_description_job , duty_time=duty_time_job)
        Emp_job.save()


        # expirence
        organization_expirence=request.POST.get('organization_expirence')
        adress_expirence=request.POST.get('adress_expirence')
        Designation_expirence=request.POST.get('Designation_expirence')
        joining_date_expirence=request.POST.get('joining_date_expirence')
        leaving_date_expirence=request.POST.get('leaving_date_expirence')
        Emp_experience = emp_experience(emp_id=emp_id,organization=organization_expirence , adress =adress_expirence , Designation=Designation_expirence , joining_date=joining_date_expirence , leaving_date = leaving_date_expirence )
        Emp_experience.save()


        # education
        title_education=request.POST.get('title_education')
        institute_education=request.POST.get('institute_education')
        board_education=request.POST.get('board_education')
        year_of_passing_education=request.POST.get('year_of_passing_education')
        persentage_education=request.POST.get('persentage_education')
        t_marks_education=request.POST.get('t_marks_education')
        o_marks_education=request.POST.get('o_marks_education')
        Emp_education = emp_education(emp_id=emp_id,title=title_education , institute =institute_education , board=board_education , year_of_passing=year_of_passing_education , persentage=persentage_education , t_marks=t_marks_education , o_marks=o_marks_education )
        Emp_education.save()



    return render(request, "e_add.html")



def e_show(request):
    allTasks = emp_personal.objects.all()
    allTasks2 = emp_education.objects.all()
    allTasks3= emp_emergency.objects.all()
    allTasks4 = emp_medical.objects.all()
    allTasks5 = emp_courses.objects.all()
    allTasks6 = emp_experience.objects.all()
    allTasks7 = emp_job.objects.all()
    context ={'task':allTasks ,'task2':allTasks2  ,'task3':allTasks3  ,'task4':allTasks4  ,'task5':allTasks5  ,'task6':allTasks6  ,'task7':allTasks7}
    return render(request, "e_show.html" , context)



    
def v_register(request):
    allTasks = Register_Vehicle.objects.all()
    context ={'task':allTasks }
    if request.method == "POST":
        vehicleid=request.POST.get('vehicleid')
        brand=request.POST.get('brand')
        engine_no=request.POST.get('engine_no')
        body_no=request.POST.get('body_no')
        engine_pwr=request.POST.get('engine_pwr')
        colour=request.POST.get('colour')
        capsity=request.POST.get('capsity')
        date1=request.POST.get('date1')
   
        Registerr_Vehicle = Register_Vehicle(vehicleid=vehicleid,brand=brand , engine_no =engine_no , body_no=body_no , engine_pwr=engine_pwr , colour = colour , capsity=capsity , date1 = date1 )
        Registerr_Vehicle.save()
    return render(request, "v_register.html" , context)



def v_route(request):
    allTasks = route.objects.all()
    allTasks1 = stop.objects.all()
    context ={'task':allTasks , 'task1':allTasks1 }
    if request.method == "POST":
        rid=request.POST.get('rid')
        session=request.POST.get('session')
        v_id=request.POST.get('v_id')
        city=request.POST.get('city')
        routes=request.POST.get('routes')
        stop2=request.POST.get('stop')
        time=request.POST.get('time')
   
        Route = route(rid=rid,session=session , v_id =v_id , routes=routes, city=city , stop=stop2 ,time=time )
        Route.save()
        return HttpResponseRedirect('/v_route/')
    return render(request, "v_route.html" ,context)

    

def v_maintenance(request):
    allTasks = maintenance.objects.all()
    context ={'task':allTasks }
    if request.method == "POST":
        id=request.POST.get('id')
        driver_id=request.POST.get('driver_id')
        vid=request.POST.get('vid')
        meachanice_id=request.POST.get('meachanice_id')
        problem=request.POST.get('problem')
        workdone=request.POST.get('workdone')
        ewr=request.POST.get('ewr')
        date1=request.POST.get('date1')
   
        Maintenance = maintenance(id=id,driver_id=driver_id , vid =vid , meachanice_id=meachanice_id, problem=problem , workdone=workdone  , ewr=ewr  , date1=date1)
        Maintenance.save()
        return HttpResponseRedirect('/v_maintenance/')
    return render(request, "v_maintenance.html" , context)




def v_vmo(request):
    return render(request, "v_vmo.html")











# add minor
def m_city(request):
    allTasks = city.objects.all()
    context ={'task':allTasks }
    if request.method == "POST":
        cid=request.POST.get('cid')
        cname=request.POST.get('cname')
   
        City = city(cid=cid,cname=cname )
        City.save()
        return HttpResponseRedirect('/m_city/')
    return render(request, "m_city.html" , context)


def m_route(request):
    allTasks = city.objects.all()
    allTasks1 = routte.objects.all()
    context ={'task':allTasks }
    if request.method == "POST":
        cid=request.POST.get('cid')
        cname=request.POST.get('cname')
        rname=request.POST.get('rname')
   
        Routte = routte(cid=cid,cname=cname , rname=rname)
        Routte.save()
        return HttpResponseRedirect('/m_route/')
    return render(request, "m_route.html" , context)



def m_stop(request):
    allTasks = city.objects.all()
    allTasks1 = routte.objects.all()
    allTasks2 = stop.objects.all()
    context ={'task':allTasks , 'task1':allTasks1  , 'task2':allTasks2}
    if request.method == "POST":
        sid=request.POST.get('sid')
        cname=request.POST.get('cname')
        rname=request.POST.get('rname')
        sname=request.POST.get('sname')
        Stop = stop(sid=sid,cname=cname , rname=rname , sname=sname)
        Stop.save()
        return HttpResponseRedirect('/m_stop/')
    return render(request, "m_stop.html" , context)









# pdf reports 
# 1.Route pdf
def emp_pdf(request):
    allTasks = route.objects.filter(city="Sahiwal").all()
    context ={'task':allTasks}
    Template_path='route_report.html'
    response=HttpResponse(content_type='application/pdf')
    response['Content-Disposition']='filename="emp_report.pdf"'
    template=get_template(Template_path)
    html=template.render(context)
     # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response )
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>' )
    return response 



# 2.Route pdf
def okara_route_pdf(request):
    allTasks = route.objects.filter(city="okara").all()
    context ={'task':allTasks}
    Template_path='route_report.html'
    response=HttpResponse(content_type='application/pdf')
    response['Content-Disposition']='filename="emp_report.pdf"'
    template=get_template(Template_path)
    html=template.render(context)
     # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response )
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>' )
    return response 

from django.db import models

class emp_personal(models.Model):
    emp_id=models.CharField(primary_key=True, null=False ,max_length=100)
    name= models.CharField(max_length=50,null=False)
    fname=models.CharField(max_length=50,null=False)
    gender=models.CharField(max_length=15,null=False)
    dob=models.DateField(null=False)
    cnic=models.BigIntegerField(null=False)
    ph1=models.BigIntegerField(null=False)
    ph2=models.BigIntegerField(null=False)
    email=models.CharField(max_length=50,null=False)
    city=models.CharField(max_length=50,null=False)
    adress=models.CharField(max_length=100,null=False)
    postal_code=models.IntegerField(null=False)
    marital_status=models.CharField(max_length=50,null=False)
    designation=models.CharField(default=NULL, max_length=50,null=False)
    image = models.ImageField(upload_to="employee/image")

    class Meta:
        db_table="emp_personal"




class emp_medical(models.Model):
        
        emp_id=models.CharField(primary_key=True, null=False ,max_length=100)
        blood=models.CharField(max_length=3, null=False)
        organ_doner= models.CharField(max_length=10, null=False)
        disability= models.CharField(max_length=10, null=False)
        fitness= models.CharField(max_length=10, null=False)
        class Meta:
            db_table="emp_medical"



class emp_emergency(models.Model):
        emp_id=models.CharField(primary_key=True, null=False ,max_length=100)
        name=models.CharField(max_length=20, null=False)
        relation=models.CharField(max_length=20, null=False)
        adress=models.CharField(max_length=50, null=False)
        city=models.CharField(max_length=20, null=False)
        email=models.CharField(max_length=25, null=False)
        ph1=models.BigIntegerField(null=False)
        ph2=models.BigIntegerField(null=False)
        class Meta:
            db_table="emp_emergency"


    

class emp_education(models.Model):
        emp_id=models.CharField(primary_key=True, null=False ,max_length=100)
        title=models.CharField(max_length=20, null=False)
        institute=models.CharField(max_length=20, null=False)
        board=models.CharField(max_length=10, null=False)
        year_of_passing=models.IntegerField(null=False)
        persentage=models.IntegerField(null=False)
        t_marks=models.IntegerField(null=False)
        o_marks=models.IntegerField(null=False)
        class Meta:
            db_table="emp_education"



class emp_courses(models.Model):
        
        emp_id=models.CharField(primary_key=True, null=False ,max_length=100)
        title=models.CharField(max_length=20, null=False)
        institute=models.CharField(max_length=20, null=False)
        Duration=models.CharField(max_length=10)
        date_of_complition=models.DateField(null=False)
        certificate=models.CharField(max_length=50 , null=False)
        no_of_project=models.IntegerField(null=False)
        class Meta:
            db_table="emp_courses"



class emp_experience(models.Model):
        emp_id=models.CharField(primary_key=True, null=False ,max_length=100)
        organization=models.CharField(max_length=100, null=False)
        adress=models.CharField(max_length=100)
        Designation=models.CharField(max_length=100, null=False)
        joining_date=models.DateField(null=False)
        leaving_date=models.DateField(null=False)
        class Meta:
            db_table="emp_experience"




class emp_job(models.Model):
    
        emp_id=models.CharField(primary_key=True, null=False ,max_length=100)
        Designation=models.CharField(max_length=100, null=False)
        job_description=models.CharField(max_length=100, null=False)
        duty_time=models.IntegerField(null=False)
        class Meta:
            db_table="emp_job"


class student(models.Model):
        
        reg_no= models.CharField(max_length=100,primary_key=True,null=False)
        name=models.CharField(max_length=100, null=False)
        batch= models.CharField(max_length=100, null=False)
        class Meta:
            db_table="student"








# vehicle database

class Register_Vehicle(models.Model):

        vehicleid= models.CharField(max_length=30,primary_key=True,null=False)
        brand=models.CharField(max_length=20, null=False)
        engine_no=models.CharField(max_length=30, null=False)
        body_no=models.CharField(max_length=40, null=False)
        engine_pwr=models.CharField(max_length=30, null=False)
        colour=models.CharField(max_length=30, null=False)
        capsity=models.CharField(max_length=30, null=False)
        date1=models.DateField(null=False)
        class Meta:
            db_table="Register_Vehicle"



class route(models.Model):
        rid =models.AutoField(primary_key=True,null=False) 
        session= models.CharField(max_length=50,null=False)
        v_id=models.CharField(max_length=20, null=False)
        routes=models.CharField(max_length=20, null=False)
        city=models.CharField(max_length=20, null=False)
        stop=models.CharField(max_length=20, null=False)
        time=models.CharField(max_length=20, null=False , default=NULL)
        class Meta:
            db_table="route"



class maintenance(models.Model):
        id= models.AutoField(primary_key=True)
        driver_id=models.CharField(max_length=100 , null=True)
        vid=models.CharField(max_length=100 , null=True)        
        meachanice_id=models.CharField(max_length=100,null=True) 
        problem=models.CharField(max_length=5000,null=True)
        workdone=models.CharField(max_length=5000,null=True)
        ewr=models.CharField(max_length=30 , null=False)
        date1=models.DateTimeField()     
        class Meta:
            db_table="maintenance"



class city(models.Model):
        cid= models.AutoField(primary_key=True)
        cname=models.CharField(max_length=100,unique=True, null=False)
        # empid=models.CharField(max_length=100,null=True)
        # date1=models.DateTimeField(default=datetime.now)
        class Meta:
            db_table="city"


class routte(models.Model):
        cid= models.AutoField(primary_key=True)
        cname=models.CharField(max_length=100, null=False)
        rname=models.CharField(max_length=100,unique=True, null=False)
        # empid=models.CharField(max_length=100,null=True)
        # date1=models.DateTimeField(default=datetime.now)
        class Meta:
            db_table="routte"




class stop(models.Model):
        sid= models.AutoField(primary_key=True)
        cname=models.CharField(max_length=100, null=False)
        rname=models.CharField(max_length=100, null=False)
        sname=models.CharField(max_length=100, null=False)
        # empid=models.CharField(max_length=100,null=True)
        # date1=models.DateTimeField(default=datetime.now)
        class Meta:
            db_table="stop"

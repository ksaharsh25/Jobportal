from email.policy import default
from django.db import models

# Create your models here.


class Employer(models.Model):
    
    industry = models.CharField(max_length=200, null=True, blank=False)
    employer = models.CharField(blank=False, max_length=100) 
    number_of_employee = models.IntegerField(blank=False, null=True)
    established_date = models.DateField(blank=False,null=True)
    address = models.CharField(blank=False, max_length=200)
    country = models.CharField(max_length=20, null=True, blank=False)
    state = models.CharField (max_length=50,null=True, blank=False)
    city = models.CharField (max_length=50,null=True, blank=False)
    pin_code = models.IntegerField(blank=True,null=True)
    mobile_number = models.IntegerField( blank=False, unique=True)
    website = models.CharField(blank=True, max_length=200)
    email = models.EmailField(blank=False, unique=True, max_length=50)
    about_company = models.TextField(max_length=2000,blank=False)
    Facebook = models.URLField(blank=True,max_length=200)
    Twitter = models.URLField(blank=True,max_length=200)
    Linkedin = models.URLField(blank=True,max_length=200)
    Instagram = models.URLField(blank=True,max_length=200)
    Youtube = models.URLField(blank=True,max_length=200)
    Others = models.URLField(blank=True,max_length=200)
    team_size = models.IntegerField(blank=True,null=True)
    image = models.ImageField(upload_to='companyimage', null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    # profile_image = models.ImageField(upload_to='companyimage', null=True, blank=True)

    def _str_(self):
        return self.mobile_number


class JobSeeker(models.Model):
    job_seeker_id = models.CharField(max_length=50,primary_key=True,blank=False,null=False)
    full_name = models.CharField(max_length=50, null=True, blank=True)
    date_birth = models.DateField(blank=True, null=True)
    job_category = models.CharField(max_length=100,null=True, blank=True)
    gender = models.CharField(max_length=10,null=True, blank=True)
    mobile_number = models.IntegerField( blank=False, unique=True)
    otp = models.CharField(max_length=7, blank=True, null=True)
    Email = models.EmailField(null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField( max_length=50,null=True, blank=True)
    city = models.CharField( max_length=50,null=True, blank=True)
    pin_code = models.IntegerField( null=True, blank=True)
    looking_for = models.CharField(max_length=30, default='Full Time', null=True)
    workig_experiance = models.IntegerField(default=0, null=True, blank=True)
    company = models.CharField(max_length=50, null=True, blank=True)
    about_me = models.CharField(max_length=2000, null=True, blank=True)
    Address = models.CharField(max_length=300, null=True, blank=True)
    education= models.CharField(max_length=200, null=True, blank=True)
    profile_image = models.ImageField(upload_to='profileimage', null=True, blank=True)
    my_file = models.FileField(upload_to='documents', null=True, blank=True)
    password = models.CharField(max_length=50,blank=True,null=True)
    # is_phone_verified=models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def _str_(self):
        return self.Mobile_number
            
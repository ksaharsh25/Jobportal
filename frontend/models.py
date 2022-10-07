from distutils.command.upload import upload
from email.policy import default
from pickle import TRUE
from django.db import models
from tinymce.models import HTMLField


classes={
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5','5'),
}


# Create your models here.
class Index(models.Model):
    company_logo=models.ImageField(upload_to='static/images/logo',null=True,blank=True)
    heading_title1=models.CharField(max_length=50,blank=False,null=True)
    heading_title2=models.CharField(max_length=50,blank=False,null=True)
    heading_description=HTMLField(max_length=500,blank=False,null=True)
    company_img1=models.ImageField(upload_to='static/images/google',null=True,blank=True)
    company_img2=models.ImageField(upload_to='static/images/microsoft',null=True,blank=True)
    mid_img=models.ImageField(upload_to='static/images/job',null=True,blank=True)
    mid_title1=models.CharField(max_length=50,blank=False,null=True)
    mid_title2=models.CharField(max_length=50,blank=False,null=True)
    mid_description=HTMLField(max_length=500,blank=False,null=True)
    scroll_title1=models.CharField(max_length=50,blank=False,null=True)
    scroll_title2=models.CharField(max_length=50,blank=False,null=True)    
    end_title1=models.CharField(max_length=50,blank=False,null=True)
    end_title2=models.CharField(max_length=50,blank=False,null=True)
    end_description=HTMLField(max_length=500,blank=False,null=True)
    about_us1=models.CharField(max_length=50,blank=False,null=True)
    about_us2=models.CharField(max_length=50,blank=False,null=True)
    footer_title1=models.CharField(max_length=50,blank=False,null=True)
    footer_title2=models.CharField(max_length=50,blank=False,null=True)
    aboutus_description=HTMLField(max_length=500,blank=False,null=True)

    def _str_(self):
        return self.logo


class PostImage(models.Model):
    post = models.ForeignKey(Index, default=None, on_delete=models.CASCADE)
    images1 = models.FileField(upload_to = 'multipleimages1/')
    images2 = models.FileField(upload_to = 'multipleimages2/')
    


class LatestBlog(models.Model):    
    blog1=models.CharField(max_length=50,blank=False,null=True)
    blog1descript=HTMLField(max_length=500,blank=False,null=True)
    blog2=models.CharField(max_length=50,blank=False,null=True)
    blog2descript=HTMLField(max_length=500,blank=False,null=True)
    blog3=models.CharField(max_length=50,blank=False,null=True)
    blog3descript=HTMLField(max_length=500,blank=False,null=True)

class AboutUs(models.Model):
    heading_title1=models.CharField(max_length=50,blank=False,null=True)
    heading_title2=models.CharField(max_length=50,blank=False,null=True)
    banner_img=models.ImageField(upload_to='static/images/banner',null=True,blank=True)
    mid_title1=models.CharField(max_length=50,blank=False,null=True)
    mid_title2=models.CharField(max_length=50,blank=False,null=True)
    mid_description=HTMLField(max_length=500,blank=False,null=True)
    # overviewtitle1=models.CharField(max_length=50,blank=False,null=True)
    # overviewtitle2=models.CharField(max_length=50,blank=False,null=True)
    # overviewdescription=HTMLField(max_length=500,blank=False,null=True)
    end_title=models.CharField(max_length=50,blank=False,null=True)

class Aboutusimage(models.Model):
    about = models.ForeignKey(AboutUs, default=None, on_delete=models.CASCADE)
    images1 = models.FileField(upload_to = 'multipleimages1/')
    images2 = models.FileField(upload_to = 'multipleimages2/')

class blog(models.Model):
    heading_title1=models.CharField(max_length=50,blank=False,null=True)
    heading_title2=models.CharField(max_length=50,blank=False,null=True)
    banner_img=models.ImageField(upload_to='static/images/banner',null=True,blank=True)
    mid_title=models.CharField(max_length=50,blank=False,null=True)
    mid_description=models.CharField(max_length=50,blank=False,null=True)
    blog1descript=HTMLField(max_length=500,blank=False,null=True)
    blog2descript=HTMLField(max_length=500,blank=False,null=True) 
    blog3descript=HTMLField(max_length=500,blank=False,null=True)
    


class contact(models.Model):    
    heading_title1=models.CharField(max_length=50,blank=False,null=True)
    heading_title2=models.CharField(max_length=50,blank=False,null=True)
    banner_img=models.ImageField(upload_to='static/images/banner',null=True,blank=True)  
    mid_title1=models.CharField(max_length=50,blank=False,null=True)
    mid_title2=models.CharField(max_length=50,blank=False,null=True)
    

class id(models.Model):
    classes=models.CharField(max_length=1,blank=True,null=True,choices=classes)




class Category(models.Model):
    category=models.ForeignKey(id,default=None,on_delete=models.CASCADE)
    heading_title1=models.CharField(max_length=50,blank=False,null=True)
    heading_title2=models.CharField(max_length=50,blank=False,null=True)
    mid_title1=models.CharField(max_length=50,blank=False,null=True)
    mid_title2=models.CharField(max_length=50,blank=False,null=True)
    end_title1=models.CharField(max_length=50,blank=False,null=True)
    end_title2=models.CharField(max_length=50,blank=False,null=True)
    footer_title1=models.CharField(max_length=50,blank=False,null=True)
    footer_title2=models.CharField(max_length=50,blank=False,null=True)
    categories=models.CharField(max_length=50,blank=False,null=True)


class background(models.Model):
    img=models.ImageField(upload_to='static/images/back',null=True,blank=True)
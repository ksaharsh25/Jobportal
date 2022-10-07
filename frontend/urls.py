from django.contrib import admin
from django.urls import path
from frontend.views import *
from . import views

urlpatterns=[
    path('index',views.index,name="index"),
    path('aboutus',aboutus,name="aboutus"),
    path('blog',log,name="blog"),
    path('contact',con,name="contact"),
    path('categories',categories,name="categories"),
    # path('employeelist',employeelist,name="employeelist"),
    path('candidatelist',candidate,name="candidatelist"),
]
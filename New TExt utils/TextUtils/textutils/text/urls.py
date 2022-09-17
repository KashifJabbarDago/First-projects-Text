from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.HomePage, name="HomePage"),
    path('result/',views.Result,name="ResultShower"),
    path('about/',views.About,name="About"),
    path('contact/',views.Contact,name="Contact")
]
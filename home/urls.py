from django.contrib import admin
from django.urls import path 
from home import views

urlpatterns = [
    path("",views.index,name="home"),
    path("e_show/",views.e_show,name="e_show"),
    path("e_show/",views.e_show,name="e_show"),
    path("v_register/",views.v_register,name="v_register"),
    path("v_route/",views.v_route,name="v_route"),
    path("v_maintenance/",views.v_maintenance,name="v_maintenance"),
    path("v_vmo/",views.v_vmo,name="v_vmo"),
    path("m_city/",views.m_city,name="m_city"),
    path("m_route/",views.m_route,name="m_route"),
    path("m_stop/",views.m_stop,name="m_stop"),



    # pdf reports
    path("create-route-sahiwal/",views.emp_pdf,name="create-route-sahiwal"),
    path("create-route-okara/",views.okara_route_pdf,name="create-route-okara"),




]

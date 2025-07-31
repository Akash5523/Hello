from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path("", views.index, name='home'),
    path("about", views.about, name='about'),
    path("toolIntegrationServices", views.toolIntegrationServices, name='toolIntegrationServices'),
    path("scriptingServices", views.scriptingServices, name='scriptingServices'),
    path("websoftdevServices", views.websoftdevServices, name='websoftdevServices'),
    path("contact", views.contact, name='contact')
]

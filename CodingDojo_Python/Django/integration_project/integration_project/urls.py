"""integration_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    # url(r'^', include('apps.ip_app.urls')),
    url(r'^time_display/', include('apps.time_display_app.timedisplay.urls')),
    url(r'^survey_form/', include('apps.survey_form_app.sf_app.urls')),
    url(r'^random_word/', include('apps.random_word_app.rwg_app.urls')),
    url(r'^login_reg/', include('apps.login_reg_app.lr_app.urls')),
    url(r'^courses/', include('apps.courses_app.c_app.urls')),
]

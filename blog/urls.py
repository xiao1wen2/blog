"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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

from django.http import HttpResponse, HttpRequest
from django.template import loader, RequestContext
from django.template.loader import get_template
from django.shortcuts import render

def index(request:HttpRequest):
    # tpl = loader.get_template('index.html')
    # context = HttpResponse()
    d = dict(zip('abcde', range(1,6)))
    # print(dct)
    return render(request, 'index.html', {'dct':d})

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index$', index),
    url(r'^user/', include("user.urls"))
]

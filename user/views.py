from django.shortcuts import render

# Create your views here.
import logging
from django.http import HttpResponse, HttpRequest, JsonResponse,HttpResponseBadRequest
import simplejson
from .models import User
FORMAT = "%(asctime)s %(threadName)s %(thread)d %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)

#sss
def reg(request:HttpRequest):
    print(request, '-------------------')
    try:
        payload = simplejson.loads(request.body.decode())
        email = payload['email']
        qs = User.objects.filter(email=email)
        print(qs)
        if qs:
            return email+"~~~~~~~~~~~~~~~~~~~~"



        password = payload['password']
        name = payload['name']

        user = User()
        user.email = email
        user.name = name
        user.password = password

        try:
            user.save()
            return JsonResponse({'user_id':user.id, 'user_name':user.name})
        except Exception as e:
            raise
    except Exception as e:
        logging.info(e)
        return HttpResponseBadRequest()
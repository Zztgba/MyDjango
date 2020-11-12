#!/usr/bin/env/python
#_*_coding:utf-8_*_
from django.http import  HttpResponse

def hello(request):
    return HttpResponse("Hello world !")
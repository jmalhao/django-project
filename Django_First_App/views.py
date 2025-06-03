from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def Django_First_App(request):
  return HttpResponse("Hello world!")

def index2(request):
  template = loader.get_template('index2.html')
  return HttpResponse(template.render())

def home(request):
  return HttpResponse("Hello world!")

def main(request):
  template = loader.get_template('main.html') # main.html ou index.html
  return HttpResponse(template.render())

def home_view(request,*args, **kwargs):
  return HttpResponse("<h1>Hello World</h1>")
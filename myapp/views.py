from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import Http404
from requests import request
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
 
 
def index(request):
  return HttpResponse("Hello test api")


class Donordata(APIView):
  def post(self, request):
    try:
      name = request.data['name']
      email = request.data['email']
      phone = request.data['phone']
      address = request.data['address']
      upline_id = request.data['upline_id']
      data = Donordata.objects.create(name=name, email=email,phone=phone,address=address, upline_id=upline_id)
      data.save()
      return Response({"status": True, "message": "data created successfully"})
    except:
      return Response({"status": False, "message": "not found"})
     


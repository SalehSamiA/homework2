from django.http import HttpResponse
from django.shortcuts import render
from .models import  Class
from .models import  Techer
from django.core import serializers


# Create your views here.
def index(req):
 return render(req, 'Well.html')


def add(req):
 Cls = Class()
 Tec=Techer()
 Cls.Name = "Ninth grade"
 Cls.Division = "A"
 Cls.save()
 Tec.firstname="Saleh"
 Tec.lastname="Sami"
 Tec.Specialization="Computer Sience"
 Tec.save()
 return HttpResponse("<html><body><h1>WellDone</h1></body></html>")


def ShowClASS(req):
 data = Class.objects.all()
 return render(req,'CLASS.html',{"data":data})
def ShowTeacher(req):
 Data = Techer.objects.all()
 return render(req,'Teacher.html',{"Data":Data})

def api(req):
 data=Class.objects.all()
 Data=Techer.objects.all()
 outC=serializers.serialize('json',data)
 outT=serializers.serialize('json',Data)

 return HttpResponse(outC+outT)
def ADDapi(req):
 data=Class()
 data.Name=req.GET.get("Name","NULL")
 data.Division=req.GET.get("Division","NotFound")
 data.save()
 Data=Techer()
 Data.firstname=req.GET.get("firstname","")
 Data.lastname=req.GET.get("lastname","")
 Data.Specialization=req.GET.get("Specialization","")
 Data.save()
 return HttpResponse("thank you for the addition")
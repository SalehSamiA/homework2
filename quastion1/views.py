from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(req):
    return HttpResponse("<html><body><h style=color:green>wellcome To Exam 1</h1></body></html>")
def Name(req):
    return HttpResponse("<html><body><h1>Student Name:-------</h1></body></html>")
def Firstbranch(req):
    return HttpResponse("<html>"
                        "<body>"
                        "<p>"
                        "<h2>What is the value of z:</h2>"
                        " x = 5;"
                        "y = 6;"
                        "z = x + y;"
                        " </ p>"
                        "</body>"
                        "</html>")



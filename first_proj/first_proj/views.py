from django.shortcuts import HttpResponse


def home(request):
    a = 10
    b = 10
    res = a + b
    # return HttpResponse("<center><h1>Hello from 1270 Batch.</h1></center>")
    return HttpResponse(f"<center><h1>Addition of {a} + {b} = {res}</h1></center>")


def add_opt(request):
    a = 10
    b = 10
    res = a + b
    # return HttpResponse("<center><h1>Hello from 1270 Batch.</h1></center>")
    return HttpResponse(f"<center><h1>Addition of {a} + {b} = {res}</h1></center>")

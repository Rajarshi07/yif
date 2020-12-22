from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"index.html")
def about(request):
    return render(request,"about.html")
def work(request):
    return render(request,"work.html")
def team(request):
    return render(request,"team.html")
def join(request):
    return render(request,"join.html")
def login(request):
    return render(request,"login.html")

from django.shortcuts import render
from .forms import MemberForm,ContactForm
from .models import Circular,NEW,File
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login
# Create your views here.
def index(request):
    if request.method == "POST":
        contact = ContactForm(data = request.POST)
        if contact.is_valid():
            contact.save()
    a=ContactForm()
    return render(request,"index.html",{'Contact':a})
def about(request):
    return render(request,"about.html")
def work(request):
    return render(request,"work.html")
def team(request):
    return render(request,"team.html")

def join(request):
    context ={}
    # user = request.user
    form = MemberForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        form.save()
        #instance = form.save()
        # instance.isActive=False
        # instance.save()
        return HttpResponseRedirect('/')
    context['form']= form
    return render(request, "join.html", context)

def loginpage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username,password = password)
        if user:
            login(request, user)
            return HttpResponseRedirect("/management/")
        else:
            return HttpResponse('Wrong Login Credentials')
    elif request.user.is_authenticated:
        return HttpResponseRedirect("/management/")
    else:
        return render(request,"login.html")

@login_required
def management(request):
    a={}
    a['news']=NEW.objects.all()
    a['circular']= list(Circular.objects.order_by('-TimeAdded'))
    a['files']=File.objects.filter(user=request.user)
    return render(request,"manager.html",a)

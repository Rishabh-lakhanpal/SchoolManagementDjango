from django.shortcuts import render, redirect, HttpResponseRedirect
from users.forms import CustomUserCreationForm,StudForm,SForm
from django.urls import reverse
from django.contrib.auth import login
from .models import stud

# Create your views here.
def dashboard(request):
    return render(request, "users/dashboard.html")

def register(request):
    if request.method == "GET":
        return render(
            request, "users/register.html",
            {"form": CustomUserCreationForm}
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("dashboard"))

def newregister(request):
    if request.user.is_authenticated:
        title = "New Student Registration"
        form = StudForm(request.POST or None)
        
        if form.is_valid():
            name = form.cleaned_data['s_name']
            clas = form.cleaned_data['s_class']
            addr = form.cleaned_data['s_addr']
            school = form.cleaned_data['s_school']
            mail = form.cleaned_data['s_email']

            p = stud(s_name=name,s_class=clas,s_addr=addr,s_school=school,s_email=mail)
            p.save()
            return render(request,'registerdone.html',{"title":"Register Successfully"})

        context={
            "title":title,
            "form":form,
        }
        return render(request,'newregister.html',context)
    else:
        return HttpResponseRedirect('/')

def existing(request):
    if request.user.is_authenticated:
        title = "All Registered Students"
        queryset = stud.objects.all()

        context= {
            "title":title,
            "queryset":queryset,
        }
        return render(request,'existingstud.html',context)
    else:
        return HttpResponseRedirect('/')

def search(request):
    if request.user.is_authenticated:
        title= "Search Student"
        form= SForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['s_name']
            queryset = stud.objects.filter(s_name=name)
            context={
                'title':title,
                'queryset':queryset
            }
            return render(request,'existingstud.html',context)

        context={
            'title':title,
            'form':form,
        }
        return render(request,'search.html',context)
    else:
        return HttpResponseRedirect('/')
    
def delete_data(request, id):
    if request.method == 'POST':
        pi = stud.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
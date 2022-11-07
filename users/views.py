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
            name = form.cleaned_data['Name']
            classroom = form.cleaned_data['Class']
            address = form.cleaned_data['Address']
            school = form.cleaned_data['School']
            mail = form.cleaned_data['Email']

            p = stud(Name=name,Classroom=classroom,Address=address,School=school,Email=mail)
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
        form= SForm(request.POST or None)
        if form.is_valid():
            name = form.cleaned_data['Name']
            queryset = stud.objects.filter(Name=name)
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
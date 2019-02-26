from django.shortcuts import render,HttpResponse
from .models import Identity

def index(request):
    if request.method == 'POST':
            if request.POST.get('email') and request.POST.get('psw'):
                identity=Identity()
                identity.uname= request.POST.get('email')
                identity.password= request.POST.get('psw')
                identity.save()
                
                return render(request, 'agri/index.html')  

            else:
                return render(request,'agri/index.html')
    return render(request,'agri/index.html')

def register(request):
    
    return render(request,'agri/register.html')

from django.shortcuts import render,HttpResponse,redirect
from .models import Identity,Farmer
from django.db import connection
import MySQLdb

session=0
U=0
#login for the admin
def index(request):
    global session
    if session==1:
        return redirect('index_loggedin')
    if request.method=='POST':
            if request.POST.get('email_login') and request.POST.get('psw_login'):
                username=Identity.objects.values_list("uname", flat=True)
                password=Identity.objects.values_list("password", flat=True)
                if request.POST.get('email_login') in username and request.POST.get('psw_login') in password:
                    session=1
                    print(session)
                    return redirect('index_loggedin')
    return render(request,'agri/index.html')
#login page
def index_loggedin(request):
    global session
    if request.method=='POST':
        session=0
        print(session)
        return redirect('index')
    return render(request,'agri/index_loggedin.html')
#farmer registration form
def register(request):
    if request.method == 'POST':
        if request.POST.get('farmerid') and request.POST.get('uid'):
            farmer=Farmer()
            farmer.uid= request.POST.get('uid')
            farmer.farmerid= request.POST.get('farmerid')
            farmer.age= request.POST.get('age')
            farmer.sec= request.POST.get('sec')
            farmer.state= request.POST.get('state')
            farmer.district= request.POST.get('district')
            farmer.village= request.POST.get('village')
            farmer.glocation= request.POST.get('glocation')
            farmer.landref= request.POST.get('landref')
            farmer.markref= request.POST.get('markref')
            farmer.save()
            return render(request,'agri/index_loggedin.html')
    return render(request,'agri/register.html')
#farmer details updation request
def update(request):
    global U
    if request.method == 'POST':
        if request.POST.get('uid') and request.POST.get('farmerid'):
            Uid=Farmer.objects.values_list("uid", flat=True)
            Farmerid=Farmer.objects.values_list("farmerid", flat=True)
            if request.POST.get('uid') in Uid and request.POST.get('farmerid') in Farmerid:
                U=Uid
                return redirect('updateform')
    return render(request,'agri/update.html')
#farmer details update form
def updateform(request):
    global U
    farmer=Farmer.objects.filter(uid= U)
    #cursor = connection.cursor()
    if request.method == 'POST':
        if request.POST.get('age'):
            farmer.sec= request.POST.get('age')
        if request.POST.get('sec'):
            farmer.sec= request.POST.get('sec')
        if request.POST.get('state'):
            farmer.state= request.POST.get('state')
        if request.POST.get('district'):
            farmer.district= request.POST.get('district')
        if request.POST.get('village'):
            farmer.village= request.POST.get('village')
        if request.POST.get('glocation'):
            farmer.glocation= request.POST.get('glocation')
        if request.POST.get('landref'):
            farmer.landref= request.POST.get('landref')
        if request.POST.get('markref'):
            farmer.markref= request.POST.get('markref')
            farmer.save()
        else:
            return redirect('index_loggedin')
    return render(request,'agri/updateform.html')
#retrieval of farmer details
def farmerdetails(request):
    farmer=Farmer.objects.values_list()
    print(farmer)
    return render(request,'agri/farmerdetails.html',{'farmer':farmer})
#What is natural farming
def naturalfarming(request):
    return render(request,'agri/naturalfarming.html')
#what are the benefits of natural farming
def farmingbenefits(request):
    return render(request,'agri/farmingbenefits.html')

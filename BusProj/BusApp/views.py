from django.shortcuts import render,HttpResponseRedirect
from .forms import BusForm
from .models import BusTable
# Create your views here.
def BusViews1(request):
    if request.method=="POST":
        BF=BusForm(request.POST)
        if BF.is_valid():
            Nm = BF.cleaned_data['Name']
            Ag = BF.cleaned_data['Age']
            Gndr = BF.cleaned_data['Gender']
            Em = BF.cleaned_data['Email']
            Pword = BF.cleaned_data['Password']
            Phn = BF.cleaned_data['Phone']
            Dj =BF.cleaned_data['Doj']
            Fm = BF.cleaned_data['From']
            T = BF.cleaned_data['To']
            data=BusTable(Name=Nm,Age=Ag,Gender=Gndr,Email=Em,Password=Pword,Phone=Phn,Doj=Dj,From=Fm,To=T)
            data.save()
            BF = BusForm()
    else:
        BF = BusForm()
    dt=BusTable.objects.all()
    return render(request,'first.html',{'B':BF,'d':dt})
def delete_data(request,id):
    if request.method == 'POST':
            pi = BusTable.objects.get(pk=id)
            pi.delete()
            return HttpResponseRedirect('/')
def update_data(request,id):
    if request.method=="POST":
        pi=BusTable.objects.get(pk=id)
        bf = BusForm(request.POST,instance=pi)
        if bf.is_valid():
            bf.save()

    else:
        pi=BusTable.objects.get(pk=id)
        bf = BusForm(instance=pi)
    return render(request,'second.html',{'B':bf})





from django.shortcuts import render
from . import models
# Create your views here.
def fun1(request):
    #data = models.Student2(name='shiva',email='srinitha@gmail.com',Dte='2012-12-12')
    #data.save()
    st=models.Student2.objects.all()
    return render(request,"first.html",{"st":st})

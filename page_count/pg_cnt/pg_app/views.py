from django.shortcuts import render

# Create your views here.
count=0
def fun(request):
    global count
    rate=0
    if request.method=="POST":
        rate = 5
        count+=1
        rate *= count
    return render(request,'pg.html',{"count":count,"rate":rate})

from django.shortcuts import render

# Create your views here.
def a2nested(request):
    d={'a':300,'b':500,'c':100}
    return render(request,'a2nested.html',d)

def a2for(request):
    d={'name':'DHONI'}
    return render(request,'a2for.html',d)
from django.shortcuts import render

# Create your views here.
def a1ifelse(request):
    d={'a':777,'b':10928}
    return render(request,'a1ifelse.html',d)

def a1ifelif(request):
    d={'a':78,'b':900,'c':1200}
    return render(request,'a1ifelif.html',d)
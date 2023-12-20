from django.shortcuts import render

# Create your views here.
def condition1(request):
    d={'a':20}
    return render(request,'condition.html',d)

def condition2(request):
    x={'a':'30'}
    return render(request,'condition.html',x)
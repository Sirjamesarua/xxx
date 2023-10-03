from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def members(request):
    # return HttpResponse('hello james')
    return render(request,'index.html')

def james(request):
    # return HttpResponse('hello james')
    return render(request,'james.html')

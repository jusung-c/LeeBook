from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def hello_world(request):
    # HttpRestponse는 response를 직접 만들어서 되돌려주는 형태
    # return HttpResponse('Hello World!')

    return render(request, 'base.html')
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from accountapp.models import HelloWorld


def hello_world(request):
    # HttpRestponse는 response를 직접 만들어서 되돌려주는 형태
    # return HttpResponse('Hello World!')

    if request.method == "POST":

        temp = request.POST.get('hello_world_input')

        # HelloWorld라는 빵 틀에서 나온 새로운 객체가 저장된다.
        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save()

        return HttpResponseRedirect(reverse('accountapp:hello_world'))
    else:
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list})
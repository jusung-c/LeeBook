from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView

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


class AccountCreateView(CreateView):
    model = User # 장고에서 기본 제공하는 User 모델

    # 장고에서 제공하는 폼
    form_class = UserCreationForm

    # 계정 만들기에 성공했다면 어느 경로로 다시 연결해줄 것인지 지정
    # reverse_lazy와 reverse의 차이는 함수형 뷰 / 클래스형 뷰 의 차이이다.
    success_url = reverse_lazy('accountapp:hello_world')

    # 회원가입할 때 볼 UI
    template_name = 'accountapp/create.html'

class AccountDetailView(DetailView):
    model = User
    # 다른 pk로 접속해도 target_user의 정보를 볼 수 있도록 지정해준다.
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'
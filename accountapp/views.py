from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render

from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.views.generic.list import MultipleObjectMixin

from accountapp.decorators import account_ownership_required
from accountapp.forms import AccountUpdateForm
from accountapp.models import HelloWorld

# 가독성을 위해 배열로 묶어서 데코레이터를 적용시킨다.
from articleapp.models import Article

has_ownership = [account_ownership_required, login_required]

@login_required
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

class AccountDetailView(DetailView, MultipleObjectMixin):
    model = User
    # 다른 pk로 접속해도 target_user의 정보를 볼 수 있도록 지정해준다.
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'

    paginate_by = 25

    def get_context_data(self, **kwargs):
        object_list = Article.objects.filter(writer=self.get_object())
        return super(AccountDetailView, self).get_context_data(object_list=object_list, **kwargs)


# method_decorator: 일반 function을 사용하는 데코레이터를 메소드에 사용할 수 있도록 변환해주는 데코레이터
@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountUpdateView(UpdateView):
    model = User
    context_object_name = 'target_user'
    form_class = AccountUpdateForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/update.html'

    # 아래의 인증 확인 절차를 데코레이터로 코딩해서 가독성을 올린다.
    # def get(self, *args, **kwargs):
    #     if self.request.user.is_authenticated and self.get_object() == self.request.user:
    #         return super().get(*args, **kwargs)
    #     else:
    #         return HttpResponseForbidden()
    #
    # def post(self, *args, **kwargs):
    #     if self.request.user.is_authenticated and self.get_object() == self.request.user:
    #         return super().post(*args, **kwargs)
    #     else:
    #         return HttpResponseForbidden()

@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'
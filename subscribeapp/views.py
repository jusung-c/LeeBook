from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView, ListView

# post는 굳이 없어도 된다.
from articleapp.models import Article
from projectapp.models import Project
from subscribeapp.models import Subscription

# 로그인을 해야 구독을 할 수 있도록
@method_decorator(login_required, 'get')
class SubscriptionView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse('projectapp:detail', kwargs={'pk': self.request.GET.get('project_pk')})


    def get(self, request, *args, **kwargs):
        project = get_object_or_404(Project, pk=self.request.GET.get('project_pk'))
        user= self.request.user

        subscription = Subscription.objects.filter(user=user,
                                                   project=project)

        # 구독했으면 없애고 안했으면 해주고
        if subscription.exists():
            subscription.delete()
        else:
            Subscription(user=user, project=project).save()

        return super(SubscriptionView, self).get(request, *args, **kwargs)


@method_decorator(login_required, 'get')
class SubscriptionListView(ListView):
    model = Article
    context_object_name = 'article_list'
    template_name = 'subscribeapp/list.html'
    paginate_by = 5

    # 특정 조건을 만족하는 게시글을 가져와야 하기 때문에 queryset 관련 함수를 새로 작성한다.
    def get_queryset(self):
        # user가 구독하고 있는 프로젝트 찾기
        projects = Subscription.objects.filter(user=self.request.user).values_list('project')

        # 프로젝트 안 모든 게시글 가져오기
        article_list = Article.objects.filter(project__in=projects)
        return article_list

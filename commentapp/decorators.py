from django.http import HttpResponseForbidden

from articleapp.models import Article
from commentapp.models import Comment


def comment_ownership_required(func):
    def decorated(request, *args, **kwargs):

        # 본인인지 확인하는 작업
        comment = Comment.objects.get(pk=kwargs['pk'])
        if not comment.writer == request.user:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)
    return decorated
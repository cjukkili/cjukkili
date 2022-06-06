from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q, Count

from board.models import Question, Comment

@login_required(login_url='common:login')
def index(request):
    question_list = Question.objects.filter(
        Q(author_id=request.user.id)
    ).order_by('-create_date')
    page = request.GET.get('page', '1')  # 페이지

    comment_list = Comment.objects.filter(
        Q(author_id=request.user)
    ).order_by('-create_date')

    # 페이징 처리
    paginator = Paginator(question_list, 10)  # 한 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    context = {'question_list': page_obj, 'comment_list':comment_list,'page': page}
    return render(request, 'mypage/profile.html', context)

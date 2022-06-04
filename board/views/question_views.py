from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator

from board.models import Question
from common.models import College


def question_college_list(request, college):
    question_list = Question.objects.filter(college_id=college).order_by('-create_date')
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')  # 검색어
    so = request.GET.get('so', 'recent')  # 정렬 기준

    # 페이징 처리
    paginator = Paginator(question_list, 10)  # 한 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    college_list = College.objects.order_by('department')
    context = {'question_list': page_obj, 'college_list': college_list, 'college': college, 'page': page, 'kw': kw, 'so': so}
    return render(request, 'board/question_list.html', context)

@login_required(login_url='common:login')
def question_like(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user == question.author:
        from django.contrib import messages
        messages.error(request, '본인이 작성한 글은 추천할수 없습니다')
    else:
        question.like.add(request.user)
    return redirect('board:detail', question_id=question.id)
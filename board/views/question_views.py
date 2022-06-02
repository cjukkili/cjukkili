from django.shortcuts import render, get_object_or_404
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

from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q, Count

from board.models import Question
from common.models import College


def index(request):
    question_list = Question.objects.order_by('-create_date')
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')  # 검색어
    so = request.GET.get('so', '')  # 정렬 기준

    # 페이징 처리
    paginator = Paginator(question_list, 10)  # 한 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    college_list = College.objects.order_by('department')
    context = {'question_list': page_obj,'college_list': college_list, 'page': page, 'kw': kw, 'so': so}
    return render(request, 'board/question_list.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')  # 검색어
    so = request.GET.get('so', 'recent')  # 정렬 기준
    college_list = College.objects.order_by('department')

    question.views += 1
    question.save()
    context = {'question': question, 'college_list': college_list, 'page': page, 'kw': kw, 'so': so}
    return render(request, 'board/question_detail.html', context)

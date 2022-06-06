from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q, Count

from board.models import Question, Category
from common.models import College


def index(request):
    question_list = Question.objects.filter(
        Q(board_type_id='free')
    ).order_by('-create_date')
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')  # 검색어
    so = request.GET.get('so', 'recent')  # 정렬 기준

    question_num = question_list.count()

    # 페이징 처리
    paginator = Paginator(question_list, 10)  # 한 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    college_list = College.objects.order_by('department')
    category_list = Category.objects.order_by('category_name')
    context = {'question_list': page_obj,'college_list': college_list, 'category_list': category_list, 'page': page, 'kw': kw, 'so': so}
    return render(request, 'free/free_list.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')  # 검색어
    so = request.GET.get('so', 'recent')  # 정렬 기준
    college_list = College.objects.order_by('department')

    question.views += 1
    question.save()
    context = {'question': question, 'page': page, 'kw': kw, 'so': so}
    return render(request, 'free/free_detail.html', context)


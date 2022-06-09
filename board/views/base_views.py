from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from board.models import Question
from common.models import College

@login_required(login_url='common:login')
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


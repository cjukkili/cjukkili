from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.utils import timezone
from board.models import Question
from common.models import College, User
from board.forms import QuestionForm
from django.contrib import messages


def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            user = User.objects.get(pk=request.user.id)
            question.author = request.user
            # question.college = user.college
            question.save()
            return redirect('board:index')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'board/question_form.html', context)


def question_college_list(request):
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')  # 검색어
    college_name = request.GET.get('college_name', '')  # 정렬 기준
    if college_name:
        question_list = Question.objects.filter(college_id=college_name).order_by('-create_date')
    else:
        question_list = Question.objects.order_by('-create_date')


    if kw:
        question_list = question_list.filter(
            Q(title__icontains=kw) |
            Q(content__icontains=kw)
        ).distinct()
    question_num = question_list.count()
    # 페이징 처리
    paginator = Paginator(question_list, 10)  # 한 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    college_list = College.objects.order_by('department')
    context = {'question_list': page_obj, 'college_list': college_list, 'question_num': question_num,
               'page': page, 'kw': kw, 'college_name': college_name}
    return render(request, 'board/question_list.html', context)


@login_required(login_url='common:login')
def question_modify(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('board:detail', question_id=question.id)
    if request.method == "POST":
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            img = request.FILES["imgs"]
            question.imgs = img
            question = form.save(commit=False)
            question.save()
            return redirect('board:detail', question_id=question.id)
    else:
        form = QuestionForm(instance=question)
    context = {'form': form}
    return render(request, 'board/question_form.html', context)

@login_required(login_url='common:login')
def question_delete(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('board:detail', question_id=question.id)
    question.delete()
    return redirect('board:index')



@login_required(login_url='common:login')
def question_like(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user == question.author:
        from django.contrib import messages
        messages.error(request, '본인이 작성한 글은 추천할수 없습니다')
    else:
        question.like.add(request.user)
    return redirect('board:detail', question_id=question.id)
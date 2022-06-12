from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from board.models import Question, BoardType
from club.forms import ClubQuestionForm
from common.models import College
from django.contrib import messages


@login_required(login_url='common:login')
def question_create(request):
    if request.method == 'POST':
        img = request.FILES.get('imgs')
        form = ClubQuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.imgs = img
            board = BoardType.objects.get(target='club')
            question.board_type = board
            question.save()
            return redirect('club:index')
    else:
        form = ClubQuestionForm()
    context = {'form': form}
    return render(request, 'club/club_form.html', context)


@login_required(login_url='common:login')
def question_college_list(request):
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')  # 검색어
    board = BoardType.objects.get(target='club')

    question_list = Question.objects.filter(board_type=board).order_by('-create_date')

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
               'page': page, 'kw': kw}
    return render(request, 'club/club_list.html', context)


@login_required(login_url='common:login')
def question_modify(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('board:detail', question_id=question.id)
    if request.method == "POST":
        form = ClubQuestionForm(request.POST, instance=question)
        if form.is_valid():
            img = request.FILES.get('imgs')
            if img:
                question.imgs = img
            question = form.save(commit=False)
            question.save()
            return redirect('board:detail', question_id=question.id)
    else:
        form = ClubQuestionForm(instance=question)
    context = {'form': form}
    return render(request, 'club/club_form.html', context)


@login_required(login_url='common:login')
def question_delete(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('club:detail', question_id=question.id)
    question.delete()
    return redirect('club:index')


@login_required(login_url='common:login')
def question_like(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user == question.author:
        from django.contrib import messages
        messages.error(request, '본인이 작성한 글은 추천할수 없습니다')
    else:
        question.like.add(request.user)
    return redirect('club:detail', question_id=question.id)
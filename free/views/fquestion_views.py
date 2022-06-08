from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from board.models import Question, Category, BoardType
from django.contrib import messages

from free.forms import FreeQuestionForm

@login_required(login_url='common:login')
def question_create(request):
    if request.method == 'POST':
        img = request.FILES.get('imgs')
        form = FreeQuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.imgs = img
            board = BoardType.objects.get(target='free')
            question.board_type = board
            question.save()
            return redirect('free:index')
    else:
        form = FreeQuestionForm()
    context = {'form': form}
    return render(request, 'free/free_form.html', context)


@login_required(login_url='common:login')
def question_free_list(request):
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')  # 검색어
    category_name = request.GET.get('category_name', '')  # 정렬 기준
    board = BoardType.objects.get(target='free')
    st = request.GET.get('searchType', '')  # 검색 기준
    if category_name:
        category_name = Category.objects.get(category_name=category_name)  # 정렬 기준
        q = Q()
        q.add(Q(board_type_id=board.id), q.AND)
        q.add(Q(category_id=category_name), q.AND)
        question_list = Question.objects.filter(q).order_by('-create_date')
    else:
        question_list = Question.objects.filter(board_type=board).order_by('-create_date')

    if kw:
        print(st)
        if st == '2':
            question_list = question_list.filter(
                Q(title__icontains=kw)).distinct()
        elif st == '3':
            question_list = question_list.filter(
                Q(content__icontains=kw)).distinct()
        else:

            question_list = question_list.filter(
                Q(title__icontains=kw) |
                Q(content__icontains=kw)
            ).distinct()

    question_num = question_list.count()
    # 페이징 처리
    paginator = Paginator(question_list, 10)  # 한 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    category_list = Category.objects.order_by('category_name')
    context = {'question_list': page_obj, 'category_list': category_list, 'question_num': question_num,
               'page': page, 'kw': kw, 'searchType': st, 'category_name': category_name}
    return render(request, 'free/free_list.html', context)


@login_required(login_url='common:login')
def question_modify(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('free:detail', question_id=question.id)
    if request.method == "POST":
        form = FreeQuestionForm(request.POST, instance=question)
        if form.is_valid():
            img = request.FILES.get('imgs')
            question.imgs = img
            question = form.save(commit=False)
            question.save()
            return redirect('free:detail', question_id=question.id)
    else:
        form = FreeQuestionForm(instance=question)
    context = {'form': form}
    return render(request, 'free/free_form.html', context)

@login_required(login_url='common:login')
def question_delete(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('free:detail', question_id=question.id)
    question.delete()
    return redirect('free:index')



@login_required(login_url='common:login')
def question_like(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user == question.author:
        from django.contrib import messages
        messages.error(request, '본인이 작성한 글은 추천할수 없습니다')
    else:
        question.like.add(request.user)
    return redirect('free:detail', question_id=question.id)
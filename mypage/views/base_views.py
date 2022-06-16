from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q, Count

from board.models import Question, Comment
from contest.models import Contest
from trade.models import TradePost


@login_required(login_url='common:login')
def index(request):
    question_list = Question.objects.filter(
        Q(author_id=request.user.id)
    ).order_by('-create_date')
    qpage = request.GET.get('qpage', '1')  # 게시글 페이지

    comment_list = Comment.objects.filter(
        Q(author_id=request.user)
    ).order_by('-create_date')
    cpage = request.GET.get('cpage', '1')  # 게시글 페이지

    trade_list = TradePost.objects.filter(Q(author_id=request.user.id)).order_by('-create_date')
    tpage = request.GET.get('tpage', '1')

    contest_list = Contest.objects.filter(Q(author_id=request.user.id)).order_by('-registration_start_date')
    ctpage = request.GET.get('ctpage', '1')

    # 페이징 처리
    question_paginator = Paginator(question_list, 10)  # 게시글 한 페이지당 10개씩 보여주기
    question_obj = question_paginator.get_page(qpage)

    comment_paginator = Paginator(comment_list, 10)  # 댓글 한 페이지당 10개씩 보여주기
    comment_obj = comment_paginator.get_page(cpage)

    trade_paginator = Paginator(trade_list, 10)  # 장터 게시글 한 페이지당 10개씩 보여주기
    trade_obj = trade_paginator.get_page(tpage)

    contest_paginator = Paginator(contest_list, 10)  # 대회글 한 페이지당 10개씩 보여주기
    contest_obj = contest_paginator.get_page(ctpage)

    context = {'question_list': question_obj, 'comment_list':comment_obj, 'qpage':qpage, 'cpage':cpage,
               'trade_list':trade_obj, 'contest_list':contest_obj, 'tpage':tpage, 'ctpage': ctpage,}
    return render(request, 'mypage/profile.html', context)

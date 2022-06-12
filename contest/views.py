from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render

from contest.models import Contest


@login_required(login_url='common:login')
def index(request):
        page = request.POST.get('page', '1')  # 페이지
        kw = request.POST.get('kw', '')  # 검색어
        contest_list = Contest.objects.order_by('registration_start_date')
        if kw:
            contest_list = contest_list.filter(
                Q(title__icontains=kw) |
                Q(content__icontains=kw)
            ).distinct()
        # 게시글 개수
        num_post = contest_list.count()
        # 페이징 처리
        paginator = Paginator(contest_list, 10)  # 한 페이지당 8개씩 보여주기
        page_obj = paginator.get_page(page) # 페이지에 있는 게시글 정보
        context = {'contest_list': page_obj, 'num_post': num_post, 'kw': kw,}
        return render(request, 'contest/contest_list.html', context)
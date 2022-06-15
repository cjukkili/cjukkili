from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.generic import CreateView

from contest.forms import ContestForm
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


class ContestCreate(LoginRequiredMixin, CreateView):
    form_class = ContestForm
    template_name = 'contest/contest_form.html'

    def test_fnc(self):
        return self.request.user.is_authenticated

    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated:
            response = super(ContestCreate, self).form_valid(form)
            return response
        else:
            return redirect('/contest/')
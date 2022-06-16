from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, DetailView, UpdateView
from django.contrib import messages
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
        paginator = Paginator(contest_list, 10)
        page_obj = paginator.get_page(page)
        context = {'contest_list': page_obj, 'num_post': num_post, 'kw': kw,}
        return render(request, 'contest/contest_list.html', context)


class ContestCreate(LoginRequiredMixin, CreateView):
    form_class = ContestForm
    template_name = 'contest/contest_form.html'

    def test_fnc(self):
        return self.request.user.is_authenticated

    def form_valid(self, form):
        current_user = self.request.user
        form.instance.author = self.request.user
        if current_user.is_authenticated:
            response = super(ContestCreate, self).form_valid(form)
            return response
        else:
            return redirect('/contest/')

class ContestDetail(LoginRequiredMixin, DetailView):
    model = Contest

    def get_context_data(self, **kwargs):
        context = super(ContestDetail, self).get_context_data()
        return context


class ContestUpdate(LoginRequiredMixin, UpdateView):
    model = Contest
    fields = ['name', 'content', 'registration_start_date', 'registration_end_date','contest_start_date',
              'contest_end_date', 'site_url',]
    template_name = 'contest/contest_modify.html'

    def form_valid(self, form):
        response = super(ContestUpdate, self).form_valid(form)
        return response

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().author:
            return super(ContestUpdate, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied

    def get_context_data(self, **kwargs):
        context = super(ContestUpdate, self).get_context_data()
        return context

def ContestDelete(request, pk):
    contest = get_object_or_404(Contest, pk=pk)
    if request.user != contest.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('contest:detail', pk=contest.id)
    contest.delete()
    return redirect('contest:index')

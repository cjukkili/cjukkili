from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.generic import CreateView, DetailView, UpdateView
from trade.forms import PostForm, CommentForm
from trade.models import TradePost, TradeComment


@login_required(login_url='common:login')
def index(request):
        page = request.POST.get('page', '1')  # 페이지
        trade_list = TradePost.objects.order_by('-create_date')
        # 게시글 개수
        num_post = trade_list.count()

        # 페이징 처리
        paginator = Paginator(trade_list, 8)  # 한 페이지당 8개씩 보여주기
        page_obj = paginator.get_page(page) # 페이지에 있는 게시글 정보
        context = {'trade_list': page_obj, 'num_post': num_post,}
        return render(request, 'trade/trade_list.html', context)


class PostCreate(LoginRequiredMixin,CreateView):

    form_class = PostForm
    template_name = 'trade/tradepost_form.html'

    def test_fnc(self):
        return self.request.user.is_authenticated

    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated:
            form.instance.author = current_user
            response = super(PostCreate, self).form_valid(form)
            return response
        else:
            return redirect('/trade/')



class PostUpdate(LoginRequiredMixin, UpdateView):
    model = TradePost
    fields = ['title', 'price', 'product_status', 'payment', 'shipping','content',  'image']
    template_name = 'trade/tradepost_modify.html'

    def form_valid(self, form):
        response = super(PostUpdate, self).form_valid(form)
        return response

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().author:
            return super(PostUpdate, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied

    def get_context_data(self, **kwargs):
        context = super(PostUpdate, self).get_context_data()
        return context


def PostDelete(request, pk):
    post = get_object_or_404(TradePost, pk=pk)
    if request.user != post.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('trade:detail', pk=post.id)
    post.delete()
    return redirect('trade:index')

class PostDetail(DetailView):
    model = TradePost

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data()
        context['comment_form'] = CommentForm
        return context


@login_required(login_url='common:login')
def new_comment(request, pk):
    if request.user.is_authenticated:
        tradepost = get_object_or_404(TradePost, pk=pk)

        if request.method == 'POST':
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.post = tradepost
                comment.author = request.user
                comment.save()
                return redirect(comment.get_absolute_url())
            else:
                return redirect(tradepost.get_absolute_url())
        else:
            raise PermissionDenied

class CommentUpdate(LoginRequiredMixin, UpdateView):
    model = TradeComment
    form_class = CommentForm
    template_name = 'trade/tradecomment_modify.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().author:
            return super(CommentUpdate, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied

def CommentDelete(request, pk):
    comment = get_object_or_404(TradeComment, pk=pk)
    if request.user != comment.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('trade:detail', pk=comment.post.id)
    comment.delete()
    return redirect('trade:detail', pk=comment.post.id)
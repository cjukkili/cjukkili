from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseNotAllowed
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import UpdateView

from board.forms import CommentForm
from board.models import Question, Comment


@login_required(login_url='common:login')
def comment_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        comment = form.save(commit=False)
        from django.utils import timezone
        comment.create_date = timezone.now()
        comment.author = request.user
        comment.question = question
        comment.save()
        return redirect('free:detail', question_id=question.id)
    else:
        return HttpResponseNotAllowed('Only POST is possible.')
    context = {'question': question, 'form': form}
    return render(request, 'free/free_detail.html', context)

class CommentUpdate(LoginRequiredMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'board/comment_modify.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user == self.get_object().author:
            return super(CommentUpdate, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied

@login_required(login_url='common:index')
def comment_delete(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    question_id = comment.question.id
    if request.user != comment.author:
        from django.contrib import messages
        messages.error(request, '삭제권한이 없습니다')
        return redirect('board:detail', question_id=question_id)
    comment.delete()
    return redirect('board:detail', question_id=question_id)
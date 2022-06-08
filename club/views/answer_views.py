from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotAllowed
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator

from board.forms import CommentForm
from board.models import Question, Comment
from common.models import College


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
        return redirect('board:detail', question_id=question.id)
    else:
        return HttpResponseNotAllowed('Only POST is possible.')
    context = {'question': question, 'form': form}
    return render(request, 'club/club_detail.html', context)

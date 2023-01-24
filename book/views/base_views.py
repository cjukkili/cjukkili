from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from book.models import Book

@login_required(login_url='common:login')
def index(request):
    bookList = Book.objects.order_by()
    page = request.GET.get('page', '1')  # 페이지
    paginator = Paginator(bookList, 10)  # 한 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'bookList': page_obj, 'page': page}

    return render(request, 'book/book_list.html', context)
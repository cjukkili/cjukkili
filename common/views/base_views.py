from dateutil.relativedelta import relativedelta
from django.shortcuts import render

from common.models import Calendar
from contest.models import Contest
from trade.models import TradePost


def index(request):
    import datetime

    today = datetime.date.today()  # 오늘
    target_date = datetime.date(2022, 6, 20)  # 종강일
    start_date = datetime.date(today.year, today.month, 1)  # 이번달 시작일
    end_date = datetime.date(today.year, today.month,1) + relativedelta(months=1) + relativedelta(days=-1)  # 이번달 마지막날
    cal = Calendar.objects.filter(start_date__range=[start_date, end_date])  # 종강일 D-Day

    trade_list = TradePost.objects.order_by('-create_date')[:5]
    contest_list = Contest.objects.order_by('registration_start_date')[:5]

    context = {'target_date': target_date, 'today': today, 'cal': cal, 'trade_list': trade_list,
               'contest_list': contest_list, }
    return render(request, 'base.html', context)
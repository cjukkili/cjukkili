from django.shortcuts import render

from common.models import College, Calendar


def index(request):
    import datetime
    today = datetime.date.today()
    target_date = datetime.date(2022,6,20)
    cal = Calendar.objects.filter(start_date__range=[datetime.date(2022,6,1),datetime.date(2022,6,30)])
    context = {'target_date':target_date, 'today':today, 'cal':cal}
    return render(request, 'base.html', context)
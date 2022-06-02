from django.shortcuts import render

from common.models import College


def index(request):
    college_list = College.objects.order_by('department')
    context = {'college_list': college_list,}
    return render(request, 'base.html', context)
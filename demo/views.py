from django.shortcuts import render
from django.http import HttpResponse, Http404


# Create your views here.

def demo(request):
    return render(request, 'demo.html')


def page(request, num):
    try:
        num = int(num)
        return render(request, 'demo.html')
    except:
        raise Http404


def home(request, year='2020', month='11'):
    return HttpResponse('获 取当前时间页签%s年/%s月' % (year, month))


def home1(request, year='2020', month='11'):
    return HttpResponse('获 取当前时间页签%s年/%s月' % (year, month))


def hom(request):
    return render(request, 'home.html')

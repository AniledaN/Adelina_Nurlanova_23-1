from django.shortcuts import HttpResponse
from datetime import date

# Create your views here.


def main(request):
    return HttpResponse()


def hello(request):
    return HttpResponse('Hello!')


def now_date(request):
    return HttpResponse(date.today())


def good_bye(request):
    return HttpResponse('goodbye!')


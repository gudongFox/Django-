//app内的视图函数
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
	return HttpResponse('<stong>hello world</strong>')

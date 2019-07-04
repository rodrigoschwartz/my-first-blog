# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

def post_list(request):
    return render(request, 'polls/post_list.html', {})
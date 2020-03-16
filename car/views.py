from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Post

# Create your views here.

def index(request):
    latest_posts_list = Post.objects.order_by('-pub_date')[:5]
    template = loader.get_template('car/index.html')
    context = {
        'latest_posts_list' : latest_posts_list,
    }
    return HttpResponse(template.render(context, request))


def detail(request, title_id):
    return HttpResponse("Title is %s." % title_id)

def results(request, title_id):
    response = "looking at results for %s"
    return HttpResponse(response % title_id)

def vote(request, title_id):
    return HttpResponse("test for %s." % title_id)
from django.shortcuts import render
from car.models import Post
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.http import HttpResponse, Http404



# Create your views here.

class PostList(generic.ListView):
    model = Post
    def get(self, request):
        post_list = Post.objects.all()
        context = {'post_list': post_list}
        return render(request, 'list.html', context=context)

class PostDetailView(DetailView):
    model = Post
    
    def get(self, request, slug):
        try:
            post = Post.objects.get(slug=slug)
        except Post.DoesNotExist:
            raise Http404("Page doesn't exsist")
        return render(request, 'page.html', {'post': post})

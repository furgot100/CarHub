from django.shortcuts import render
from posts.models import Post
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.http import HttpResponse, Http404
from django.views.generic.edit import CreateView

# Create your views here.
class PostList(ListView):
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
            raise Http404("Post doesn't exist")
        return render(request, 'post.html', {'post' : post})

class PostCreateView(CreateView):
    model = Post
    fields = Post.objects.all()
    context = {'fields' : fields}
    return render(request, 'new.html', context=context)


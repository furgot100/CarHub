from django.shortcuts import render
from posts.models import Post
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.http import HttpResponse, Http404
from django.views.generic.edit import CreateView
from posts.forms import PostCreateForm
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

# Create your views here.
class PostListView(ListView):
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
    def get(self, request, *args, **kwargs):
        post = {'form': PostCreateForm()}
        return render(request, 'new.html', post)

    def post(self, request, *args, **kwargs):
        form = PostCreateForm(request.POST)
        if form.is_valid():
            post = form.save()
            post.save()
            return HttpResponseRedirect(reverse_lazy('posts:post-list-page'))
        return render(request,'new.html', {'form': form})

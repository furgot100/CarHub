from django.shortcuts import render, get_object_or_404
from posts.models import Post, Products, Event
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.http import HttpResponse, Http404
from django.views.generic.edit import CreateView
from posts.forms import PostCreateForm, ProductCreateForm, EventCreateForm
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, DeleteView

# Create your views here.
class PostListView(ListView):
    model = Post
    def get(self, request):
        post_list = Post.objects.all()
        context = {'post_list': post_list}
        return render(request, 'blog/list.html', context=context)

class PostDetailView(DetailView):
    model = Post

    def get(self, request, slug):
        try:
            post = Post.objects.get(slug=slug)
        except Post.DoesNotExist:
            raise Http404("Post doesn't exist")
        return render(request, 'blog/post.html', {'post' : post})

class PostCreateView(CreateView):
    def get(self, request, *args, **kwargs):
        post = {'form': PostCreateForm()}
        return render(request, 'blog/new.html', post)

    def post(self, request, *args, **kwargs):
        form = PostCreateForm(request.POST)
        if form.is_valid():
            post = form.save()
            post.save()
            return HttpResponseRedirect(reverse_lazy('posts:post-list-page'))
        return render(request,'blog/new.html', {'form': form})


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "CarHub"
        return context



class PostDeleteView(DeleteView):
    model = Post

    def get(self, request, slug):
        try:
            post = Post.objects.get(slug=slug)
        except Post.DoesNotExist:
            raise Http404("Post doesn't exist")
        return render(request, 'delete.html', {'post' : post})

# Parts/Store

class ProductListView(ListView):
    model = Products
    def get(self, request):
        store_list = Products.objects.all()
        context = {'store_list': store_list}
        return render(request, 'store/list.html', context=context)

class ProductDetailView(DetailView):
    model = Products

    def get(self, request, slug):
        try:
            product = Products.objects.get(slug=slug)
        except Products.DoesNotExist:
            raise Http404("Product doesn't exist")
        return render(request, 'store/item.html', {'product' : product})


class ProductCreateView(CreateView):
    def get(self, request, *args, **kwargs):
        product = {'form': ProductCreateForm()}
        return render(request, 'store/new_item.html', product)

    def post(self, request, *args, **kwargs):
        form = ProductCreateForm(request.POST)
        if form.is_valid():
            item = form.save()
            item.save()
            return HttpResponseRedirect(reverse_lazy('posts:store-list'))
        return render(request,'store/new_item.html', {'form': form})

# Events
class EventListView(ListView):
    model = Event
    def get(self, request):
        event_list = Event.objects.all()
        context = {'event_list': event_list}
        return render(request, 'evnt/list.html', context=context)

class EventDetailView(DetailView):
    model = Event

    def get(self, request, slug):
        try:
            event = Event.objects.get(slug=slug)
        except Products.DoesNotExist:
            raise Http404("Product doesn't exist")
        return render(request, 'evnt/event.html', {'event' : event})

class EventCreateView(CreateView):
    def get(self, request, *args, **kwargs):
        event = {'form': EventCreateForm()}
        return render(request, 'evnt/new_event.html', event)

    def post(self, request, *args, **kwargs):
        form = EventCreateForm(request.POST)
        if form.is_valid():
            item = form.save()
            item.save()
            return HttpResponseRedirect(reverse_lazy('posts:event-list'))
        return render(request,'evnt/new_event.html', {'form': form})





      


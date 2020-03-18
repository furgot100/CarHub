from django.urls import path
from .views import PostCreateView, PostDetailView, PostListView


app_name = 'posts'
urlpatterns = [
    path('blog', PostListView.as_view(), name='post-list-page'),
    path('new/', PostCreateView.as_view(), name='post-new-page' ),
    path('<slug>/', PostDetailView.as_view(), name='post-details-page'),
]
from django.urls import path
from . import views


app_name = 'posts'
urlpatterns = [
    path('blog', views.PostList.as_view(), name='post-list-page'),
    path('new/',views.PostCreateView.as_view(), name='post-new-page' ),
    path('<str:slug>/', views.PostDetailView.as_view(), name='post-details-page'),
]
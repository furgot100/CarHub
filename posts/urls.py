from django.urls import path
from . import views

urlpatterns = [
    path('blog', views.PostList.as_view(), name='post-list-page'),
    path('<str:slug>/', views.PostDetailView.as_view(), name='post-details-page'),
]
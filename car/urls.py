from django.urls import path

from . import views

app_name = 'car'
urlpatterns = [
    path('', views.PostList.as_view(), name='post-list'),
    path('<slug>/', views.PostDetailView.as_view(), name='post-detail')
]
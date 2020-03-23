from django.urls import path
from .views import PostCreateView, PostDetailView, PostListView, HomeView, PostDeleteView, ProductListView, ProductDetailView

app_name = 'posts'
urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('blog/', PostListView.as_view(), name='post-list-page'),
    path('new/', PostCreateView.as_view(), name='post-new-page' ),
    path('blog/<str:slug>/', PostDetailView.as_view(), name='post-details-page'),
    # path('<slug>/delete', PostDeleteView.as_view(), name='post-delete-page')
    path('store/', ProductListView.as_view(), name="store-list"),
    path('store/<str:slug>/', ProductDetailView.as_view(), name='store-item'),
]
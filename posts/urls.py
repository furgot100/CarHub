from django.urls import path
from .views import PostCreateView, PostDetailView, PostListView, HomeView, PostDeleteView, ProductListView, ProductDetailView, ProductCreateView
from django.conf import settings
from django.conf.urls.static import static

app_name = 'posts'
urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('blog/', PostListView.as_view(), name='post-list-page'),
    path('new/', PostCreateView.as_view(), name='post-new-page' ),
    path('blog/<str:slug>/', PostDetailView.as_view(), name='post-details-page'),
    # path('<slug>/delete', PostDeleteView.as_view(), name='post-delete-page')
    path('store/', ProductListView.as_view(), name="store-list"),
    path('store/<str:slug>/', ProductDetailView.as_view(), name='store-item'),
    path('store/new', ProductCreateView.as_view(), name='store-new'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
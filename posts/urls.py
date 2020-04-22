from django.urls import path
from .views import PostCreateView, PostDetailView, PostListView, HomeView, PostDeleteView, ProductListView, ProductDetailView, ProductCreateView, EventListView, EventDetailView, EventCreateView
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
    path('event/', EventListView.as_view(), name="event-list"),
    path('event/<str:slug>/', EventDetailView.as_view(), name="event-detail"),
    path('event/new', EventCreateView.as_view(), name='event-new'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.urls import path

from . import views

app_name = 'car'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:title_id>/', views.DetailView.as_view(), name='detail'),
    path('<int:title_id>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:title_id>/vote/', views.vote, name='vote'),
]
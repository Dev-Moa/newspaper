from django.urls import path
from .views import ArticleListView,articleEditView,articleDeleteView,articleCreateView,ArticleDetailView
urlpatterns=[
    path('articles/<int:pk>/delete',articleDeleteView.as_view(),name='article_delete'),
    path('articles/<int:pk>/edit/',articleEditView.as_view(),name="article_edit"),
    path('articles/new/',articleCreateView.as_view(),name='article_create'),
    path('articles/<int:pk>/',ArticleDetailView.as_view(),name="article_detail"),
    path('',ArticleListView.as_view(),name='articles')
]
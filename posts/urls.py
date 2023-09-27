from schema_graph.views import Schema
from django.urls import path
from posts import views
from .views import create_tag, TagListView


urlpatterns = [
	path("schema/", Schema.as_view()),
	path('posts/', views.PostList.as_view()),
	path('posts/<int:pk>/', views.PostDetail.as_view()),
	#path('posts/tags/', views.TagsList.as_view())
    path('posts/create-tag/', create_tag, name='create_tag'),
    path('posts/tags/', TagListView.as_view(), name='tag-list'),
]
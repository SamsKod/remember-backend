from schema_graph.views import Schema
from django.urls import path
from posts import views

urlpatterns = [
	path("schema/", Schema.as_view()),
	path('posts/', views.PostList.as_view()),
	path('posts/<int:pk>/', views.PostDetail.as_view()),
	path('posts/tags/', views.TagsList.as_view())
]
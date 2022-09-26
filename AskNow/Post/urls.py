from django.urls import path
from Post.views import CreatePost, PostDetailView, UpdatePost, DeletePost, MyPosts


urlpatterns = [
    path('creat-post/', CreatePost.as_view(), name='creat_post'),
    path('<str:slug>/', PostDetailView.as_view(), name='post_detail'),
    path('edit/<str:slug>/', UpdatePost.as_view(), name='update_post'),
    path('<str:slug>/delete/', DeletePost.as_view(), name='delete_post'),
    path('my-posts', MyPosts.as_view(), name='view_mypost'),
]

from django.contrib import admin
from django.urls import path, include
from reddit.main_views import HomeView, LikeView, CommentView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('User.urls')),
    path('home/', HomeView.as_view(), name='home'),
    path('post/', include('Post.urls')),
    path('like/', LikeView.as_view(), name='like_post'),
    path('comment/', CommentView.as_view(), name='comment_post'),
]

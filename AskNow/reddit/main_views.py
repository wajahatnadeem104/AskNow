from django.views.generic import ListView, View
from Post.models import Post, Comment
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.utils.timezone import datetime
from datetime import timedelta


class HomeView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'home.html'

    def get_queryset(self):
        qs = Post.objects.all().order_by('-date_published')
        return sorted(qs, key=lambda a: a.total_votes(), reverse=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        today = datetime.today().date()
        top_today_posts = Post.objects.filter(
            date_published__date=today).order_by('-date_published')
        context['top_post_today'] = sorted(
            top_today_posts, key=lambda a: a.total_votes(), reverse=True)[:10]
        context['my_posts_today'] = Post.objects.filter(
            author=self.request.user.id, date_published__date=today).order_by('-date_published')
        context['my_posts_yesterday'] = Post.objects.filter(
            author=self.request.user.id, date_published__date=today-timedelta(days=1)).order_by('-date_published')
        return context


class LikeView(LoginRequiredMixin, View):

    def get(self,request):
        blog_post = get_object_or_404(Post, id=request.GET.get('post_id'))
        if request.GET.get('vote_type') == 'upvote':
            if blog_post.downvotes.filter(id=request.user.id).exists():
                blog_post.downvotes.remove(request.user)
                blog_post.upvotes.add(request.user)
            elif blog_post.upvotes.filter(id=request.user.id).exists():
                blog_post.upvotes.remove(request.user)
            else:
                blog_post.upvotes.add(request.user)
        elif request.GET.get('vote_type') == 'downvote':
            if blog_post.upvotes.filter(id=request.user.id).exists():
                blog_post.upvotes.remove(request.user)
                blog_post.downvotes.add(request.user)
            elif blog_post.downvotes.filter(id=request.user.id).exists():
                blog_post.downvotes.remove(request.user)
            else:
                blog_post.downvotes.add(request.user)
        response = {
            'total_votes': blog_post.total_votes(),
            'upvote': blog_post.upvotes.filter(id=request.user.id).exists(),
            'downvote' : blog_post.downvotes.filter(id=request.user.id).exists()
        }
        return JsonResponse(response)


class CommentView(LoginRequiredMixin, View):
    
    def get(request):
        cmnt_body = str(request.GET.get('cmnt_body'))
        cmnt_username = request.user.username
        post = get_object_or_404(Post, id=request.GET.get('post_id'))
        Comment.objects.create(
            blog_post=post,
            body=cmnt_body,
            username=cmnt_username
        )
        cmnt = Comment.objects.filter(
            blog_post=post, username=cmnt_username).last()
        response = {
            'cmnt_username': cmnt.username,
            'cmnt_body': cmnt.body,
            'cmnt_date_added': cmnt.date_added.date()
        }
        return JsonResponse(response)

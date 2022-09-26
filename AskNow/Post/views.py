from django.urls import reverse, reverse_lazy
from Post.form import PostForm
from Post.models import Post
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from django.utils.text import slugify
from django.contrib.auth.mixins import LoginRequiredMixin


class CreatePost(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post/create_post.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(CreatePost, self).form_valid(form)

    def get_success_url(self):
        return reverse('post_detail', kwargs={'slug': self.object.slug})


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'post/post_detail.html'


class UpdatePost(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'post/update_post.html'

    def form_valid(self, form):
        form.instance.slug = slugify(
            form.instance.author.username + '-' + form.instance.title)
        return super(UpdatePost, self).form_valid(form)

    def get_success_url(self):
        return reverse('post_detail', kwargs={'slug': self.object.slug})


class DeletePost(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'post/delete_post.html'
    success_url = reverse_lazy('view_mypost')


class MyPosts(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'post/my_post.html'
    context_object_name = 'my_posts'

    def get_queryset(self):
        user = self.request.user
        return Post.objects.filter(author=user.id).order_by('-date_published')

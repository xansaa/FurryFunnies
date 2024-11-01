from django.urls import reverse_lazy
from django.views.generic import TemplateView, DetailView, DeleteView, ListView
from FurryFunnies.posts.models import Post


class NewPost(ListView):
    model = Post
    template_name = 'post/create-post.html'

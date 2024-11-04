from django.urls import reverse_lazy
from django.views.generic import TemplateView, DetailView, DeleteView, ListView, CreateView

from FurryFunnies.author.models import Author
from FurryFunnies.posts.models import Post


class NewPost(ListView):
    model = Post
    template_name = 'post/create-post.html'


class PostCreateView(CreateView):
    model = Post
    template_name = 'post/create-post.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.author = Author.objects.first()
        return super().form_valid(form)


class 
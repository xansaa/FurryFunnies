from django.urls import reverse_lazy
from django.views.generic import TemplateView, DetailView, DeleteView


class NewPost(TemplateView):
    template_name = 'post/create-post.html'

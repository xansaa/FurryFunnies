from django.views.generic import TemplateView, CreateView, DetailView


class IndexView(TemplateView):
    template_name = 'index.html'

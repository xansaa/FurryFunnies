from django.views.generic import TemplateView, CreateView, DetailView


class IndexView(TemplateView):
    template_name = 'index.html'



class DashboardView(TemplateView):
    template_name = 'dashboard.html'

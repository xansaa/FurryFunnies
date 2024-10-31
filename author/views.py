from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, DetailView

from FurryFunnies.author.models import Author


class CreateAuthorView(CreateView):
    model = Author
    template_name = 'author/create-author.html'
    fields = ['first_name', 'last_name', 'passcode', 'pets_number']
    success_url = reverse_lazy('index')


class AuthorProfileDetails(TemplateView):
    model = Author
    template_name = 'author/details-author.html'
    

from django.urls import path
from .views import CreateAuthorView, AuthorProfileDetails

urlpatterns = [
    path('create/', CreateAuthorView.as_view(), name='create_author_profile'),
    path('details/', AuthorProfileDetails.as_view(), name='author-details'),
]








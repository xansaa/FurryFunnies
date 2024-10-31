from django.urls import path
from FurryFunnies.posts.views import NewPost

urlpatterns = [
    path('create/', NewPost.as_view(), name='create-post')


]
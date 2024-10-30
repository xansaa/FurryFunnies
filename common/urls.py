from django.urls import path
from FurryFunnies.common.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]


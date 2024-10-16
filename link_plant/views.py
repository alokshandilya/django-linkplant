from django.views.generic import ListView

from .models import Link


# Create your views here.
class LinkListView(ListView):
    model = Link

from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .models import Link


# Create your views here.
class LinkListView(ListView):
    model = Link


class LinkCreateView(CreateView):
    model = Link
    fields = "__all__"
    success_url = reverse_lazy("link-list")


class LinkUpdateView(UpdateView):
    model = Link
    fields = ["text", "url"]
    success_url = reverse_lazy("link-list")


class LinkDeleteView(DeleteView):
    model = Link
    success_url = reverse_lazy("link-list")

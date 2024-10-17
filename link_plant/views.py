from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .models import Link, Profile


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


def profile_view(request, profile_slug):
    profile = get_object_or_404(Profile, slug=profile_slug)
    links = profile.links.all()  # foreign key related name is links
    context = {
        "profile": profile,
        "links": links,
    }
    return render(request, "link_plant/profile.html", context)

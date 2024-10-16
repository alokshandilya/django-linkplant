from django.urls import path

from .views import LinkListView  # it's a class-based view

urlpatterns = [
    path("", LinkListView.as_view(), name="home"),
]

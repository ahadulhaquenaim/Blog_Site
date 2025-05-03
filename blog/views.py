from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Post
from django.views.generic import ListView, DetailView


# Create your views here.

class StartingPageView(ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "posts"
    ordering = ['-date']

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data


class AllPostsView(ListView):
    model = Post
    template_name = "blog/all-posts.html"
    context_object_name = "all_posts"
    ordering = ['-date']

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset
        return data


class SinglePostView(DetailView):
    model = Post
    template_name = "blog/post-detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_tags'] = self.object.tags.all()
        return context

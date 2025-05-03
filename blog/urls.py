from django.urls import path
from blog.views import StartingPageView, AllPostsView, SinglePostView

urlpatterns = [
    path("", StartingPageView.as_view(), name="starting-page"),  # This is the root
    path("posts", AllPostsView.as_view(), name='posts-page'),  # This is the posts page
    path("post/<slug:slug>", SinglePostView.as_view(), name='post-detail-page')  # This is the posts page
]

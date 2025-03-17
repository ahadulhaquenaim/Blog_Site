from django.urls import path
from blog import views

urlpatterns = [
    path("", views.starting_page, name="starting-page"),  # This is the root
    path("posts", views.posts, name='posts-page'),  # This is the posts page
    path("post/<slug>", views.post_detail, name='post-detail-page')  # This is the posts page
]

from django.shortcuts import render


# Create your views here.

def startingpage(request):
    return render(request, "blog/index.html")


def posts(request):
    return render(request, "blog/all-posts.html")


def post_detail(request, slug):
    return render(request, "blog/post-detail.html")

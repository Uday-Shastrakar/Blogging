from blog.models import Post
from django.shortcuts import render, get_object_or_404


# Create your views here.
def home(request):
    # load all the post from db(10)
    posts = Post.objects.all()[:11]
    # print(posts)
    data = {
        'posts': posts
    }
    return render(request, 'home.html', data)


def posts(request, url):
    post = Post.objects.get(url=url)
    # print(post)
    return render(request, 'posts.html', {'post': post})

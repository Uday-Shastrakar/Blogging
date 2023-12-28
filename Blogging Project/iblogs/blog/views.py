from blog.models import Post
from django.shortcuts import render


# Create your views here.
def home(request):
    # load all the post from db(10)
    posts = Post.objects.all()[:11]
    # print(posts)
    data = {
        'posts': posts
    }
    return render(request, 'home.html', data)

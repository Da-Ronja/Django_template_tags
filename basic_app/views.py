from .models import Post
from django.shortcuts import render, get_object_or_404

# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, 'basic_app/index.html', {'posts': posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'basic_app/post_detail.html', {'post': post})



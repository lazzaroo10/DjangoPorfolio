from django.shortcuts import render , get_object_or_404

from .models import Post
# Create your views here.

#Para poner todas a la vez
def render_posts(request):
    posts  = Post.objects.all
    return render(request,'posts.html',{'posts':posts})

#Para poner posts 1 por 1 (1 post pantalla entera)
def post_detail(request,post_id):

    post  = get_object_or_404(Post,pk = post_id)
    return render(request,'post_detail.html',{'post_id':post})

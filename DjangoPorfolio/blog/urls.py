from django.urls import path
from .views import render_posts, post_detail

app_name = 'blog'

urlpatterns = [
    path('',render_posts,name='posts'),
    #Es int porque la base de datos lo guarda como numero
    path('<int:post_id>', post_detail , name='post_detail')
]


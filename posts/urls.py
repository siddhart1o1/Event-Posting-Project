from django.urls import path
from .views import Post_view,like_post,add_post


urlpatterns = [
     path("",Post_view,name="post-list")
     ,path("like/",like_post,name = "like-post"),
     path("add_post",add_post,name = "add-post")
]

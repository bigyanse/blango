from django.urls import path

from blog.views import BlogListView, BlogDetailView, BlogCreateView

urlpatterns = [
    path("", BlogListView.as_view(), name="home"),
    path("post/new", BlogCreateView.as_view(), name="post_create"),
    path("post/<int:pk>", BlogDetailView.as_view(), name="post_detail")
]
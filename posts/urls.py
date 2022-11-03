from django.urls import path, reverse_lazy
from django.views.generic import RedirectView

from posts.views import PostDetailView, PostListView, UsersPostListView, SearchListView

urlpatterns = [
    path("posts/", PostListView.as_view(), name="post-list"),
    path("posts/search/", SearchListView.as_view(), name="post-search"),
    path("posts/<pk>/", PostDetailView.as_view(), name="post-detail"),
    path(
        "posts/author/<username>/", UsersPostListView.as_view(), name="user-post-list"
    ),
    path("", RedirectView.as_view(url=reverse_lazy("post-list"), permanent=False)),
]
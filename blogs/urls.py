from django.urls import path
from . import views

app_name = "blogs"

urlpatterns = [
    path("", views.blog_list_view, name="list"),
    path("detail/<int:blog_pk>", views.blog_detail_view, name="detail"),
    path("tag/<slug:tag>", views.blog_tag_view, name="tag"),
    path("category/<slug:category>", views.blog_category_view, name="category"),
    path("search/", views.search, name="search"),
]

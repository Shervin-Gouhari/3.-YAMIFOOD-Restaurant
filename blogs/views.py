from django.shortcuts import render, get_object_or_404
from .models import Blog, Tag, Category, BlogComment
from .forms import CommentForm
from django.core.paginator import Paginator
from django.db.models import Q

def blog_list_view(request):
    blogs = Blog.objects.all()
    paginator = Paginator(blogs, 4)
    page_number = request.GET.get('page')
    blog_list = paginator.get_page(page_number)
    return render(request, "blogs/list.html", {"blog_list": blog_list})


# "-created_at" = recent to old | "created_at" = old to recent
# [:5] = the five last blogs
def blog_detail_view(request, blog_pk):
    blog = get_object_or_404(Blog, id=blog_pk)
    tags = Tag.objects.all().filter(blogs=blog)
    recents = Blog.objects.all().order_by("-created_at")[:5]
    categories = Category.objects.all()
    comments = BlogComment.objects.all().filter(related_blog=blog)
    
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            new_name = form.cleaned_data['name']
            new_email = form.cleaned_data['email']
            new_message = form.cleaned_data['message']
            new_comment = BlogComment(
                related_blog=blog,
                name=new_name,
                email=new_email,
                comment=new_message,
            )
            new_comment.save()
    else:
        form = CommentForm()
        
    context = {
        "blog": blog,
        "tags": tags,
        "recents": recents,
        "categories": categories,
        "comments": comments,
        "comment_form": form,
    }
    return render(request, "blogs/detail.html", context)

def blog_tag_view(request, tag):
    blog_list = Blog.objects.filter(tag__slug=tag)
    return render(request, "blogs/list.html", {"blog_list": blog_list})

def blog_category_view(request, category):
    blog_list = Blog.objects.filter(category__slug=category)
    return render(request, "blogs/list.html", {"blog_list": blog_list})

def search(request):
    if request.method == "GET":
        q = request.GET.get("search", "")
        blogs = Blog.objects.filter(
            Q(title__icontains=q) |
            Q(description__icontains=q) |
            Q(content__icontains=q)
            )
        paginator = Paginator(blogs, 4)
        page_number = request.GET.get('page', '1')
        blog_list = paginator.get_page(page_number)
        return render(request, 'blogs/list.html', {'blog_list': blog_list})
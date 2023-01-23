from django.shortcuts import render, get_object_or_404
from .models import Food, FoodComment
from .forms import CommentForm

def food_list_view(request):
    food_list = Food.objects.all()
    comment_list = FoodComment.objects.all().order_by("-created_at")[:5]
    return render(request, 'foods/list.html', {"food_list": food_list, "comment_list": comment_list})

def food_detail_view(request, food_pk):
    food = get_object_or_404(Food, id=food_pk)
    comments = FoodComment.objects.all().filter(related_food=food)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = FoodComment(
                name = form.cleaned_data["name"],
                email = form.cleaned_data["email"],
                comment = form.cleaned_data["message"],
                related_food = food
            )
            new_comment.save()
    else:
        form = CommentForm()
    return render(request, 'foods/detail.html', {"food": food, "comments": comments, "comment_form": form})
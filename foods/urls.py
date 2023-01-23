from django.urls import path
from . import views

app_name = 'foods'

urlpatterns = [
    path("", views.food_list_view, name="list"),
    path("detail/<int:food_pk>", views.food_detail_view, name="detail"),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name='about'),
    path('recipes/', views.RecipeList.as_view(), name="recipe_list"),
    path('recipes/new/', views.RecipeCreate.as_view(), name="recipe_create"),
]
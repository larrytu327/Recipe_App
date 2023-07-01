from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name='about'),
    path('recipes/', views.RecipeList.as_view(), name="recipe_list"),
    path('recipes/new/', views.RecipeCreate.as_view(), name="recipe_create"),
    path('recipes/<int:pk>/', views.RecipeDetail.as_view(), name="recipe_detail"),
    path('recipes/<int:pk>/update', views.RecipeUpdate.as_view(), name="recipe_update"),
    path('recipes/<int:pk>/delete', views.RecipeDelete.as_view(), name="recipe_delete"),
]
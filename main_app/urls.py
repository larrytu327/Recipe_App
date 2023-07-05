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
    path('recipes/<int:pk>/ingredients/new/', views.IngredientCreate.as_view(), name="ingredient_create"),
    path('shoppinglists/', views.Shopping_Lists_List.as_view(), name="shopping_lists_list"),
    path('shoppinglists/<int:pk>/ingredients/<int:ingredient_pk>/', views.Shopping_ListsIngredientAssoc.as_view(), name="shopping_lists_ingredient_assoc"),
    path('shoppinglists/<int:pk>/', views.Shopping_ListDetail.as_view(), name="shopping_list_detail"),
]
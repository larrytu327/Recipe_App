from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from .models import Recipe, Ingredients, Shopping_Lists
from django.urls import reverse

class Home(TemplateView):
    template_name = "home.html"

class About(TemplateView):
    template_name = "about.html"

class RecipeList(TemplateView):
    template_name = "recipe_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get('name')
        if name != None:
            context["recipes"] = Recipe.objects.filter(name__icontains=name)
            context["header"] = f"Searching for {name}"
        else:
            context["recipes"] = Recipe.objects.all()
            context["header"] = "Recipes"
        return context
    
class RecipeCreate(CreateView):
    model = Recipe
    fields = ['name', 'img', 'description', 'instructions', 'link']
    template_name = "recipe_create.html"
    
    def get_success_url(self):
        return reverse('recipe_detail', kwargs={'pk': self.object.pk})

class RecipeDetail(DetailView):
    model = Recipe
    template_name = "recipe_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["shopping_lists"] = Shopping_Lists.objects.all()
        return context

class RecipeUpdate(UpdateView):
    model = Recipe
    fields = ['name', 'img', 'description', 'instructions', 'link']
    template_name = "recipe_update.html"
    success_url = "/recipes/"    
    # def get_success_url(self):
    #     return reverse('recipe_detail', kwargs={'pk': self.object.pk})
    
class RecipeDelete(DeleteView):
    model = Recipe
    template_name = "recipe_delete_confirmation.html"
    success_url = "/recipes/"

class IngredientCreate(View):
    def post(self, request, pk):
        name = request.POST.get("name")
        type = request.POST.get("type")
        recipe = Recipe.objects.get(pk=pk)
        Ingredients.objects.create(name=name, type=type, recipe=recipe)
        return redirect('recipe_detail', pk=pk)
    
# class Shopping_Lists(TemplateView):
#     template_name = "shopping_lists_list.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         name = self.request.GET.get('name')
#         if name != None:
#             context["shopping_lists"] = Shopping_Lists.objects.filter(name__icontains=name)
#             context["header"] = f"Searching for shopping list with name: {name}"
#         else:
#             context["shopping_lists"] = Shopping_Lists.objects.all()
#             context["header"] = "Shopping Lists"
#         return context

class Shopping_Lists_List(TemplateView):
    model = Shopping_Lists
    template_name = "shopping_lists_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["shopping_lists"] = Shopping_Lists.objects.all()
        return context
    
class Shopping_ListsIngredientAssoc(View):

    def get(self, request, pk, ingredient_pk):
        assoc = request.GET.get("assoc")
        if assoc == "remove":
            Shopping_Lists.objects.get(pk=pk).ingredients.remove(ingredient_pk)
            return redirect('shopping_lists_list')
        if assoc == "add":
            Shopping_Lists.objects.get(pk=pk).ingredients.add(ingredient_pk)
            return redirect('recipe_detail', pk=pk)
        
class Shopping_ListDetail(DetailView):
    model = Shopping_Lists
    template_name = "shopping_list_detail.html"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["shopping_lists"] = Shopping_Lists.objects.all()
    #     return context


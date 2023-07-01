from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from .models import Recipe
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

class RecipeUpdate(UpdateView):
    model = Recipe
    fields = ['name', 'img', 'descriptions', 'instructions', 'link']
    template_name = "recipe_update.html"
    
    def get_success_url(self):
        return reverse('recipe_detail', kwargs={'pk': self.object.pk})
    
class RecipeDelete(DeleteView):
    model = Recipe
    template_name = "recipe_delete_confirmation.html"
    success_url = "/recipe/"
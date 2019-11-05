from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from ChefAssist.models import Recipe, Events
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
import json

# Create your views here.
@login_required
def calendar(request):
    all_events = Events.objects.all()
    context = {
        "events":all_events,
    }
    return render(request,'calendar.html',context)
    
@login_required
def add_event(request):
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    title = request.GET.get("title", None)
    event = Events(name=str(title), start=start, end=end)
    event.save()
    data = {}
    return JsonResponse(data)

@login_required
def update(request):
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    title = request.GET.get("title", None)
    id = request.GET.get("id", None)
    event = Events.objects.get(id=id)
    event.start = start
    event.end = end
    event.name = title
    event.save()
    data = {}
    return JsonResponse(data)

@login_required
def remove(request):
    id = request.GET.get("id", None)
    event = Events.objects.get(id=id)
    event.delete()
    data = {}
    return JsonResponse(data)

def home(request):
    return render(request, "home.html")

def signup(request):
    if request.method=="POST":
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']

        exists=User.objects.filter(username=username).exists()

        if not exists:
            user=User.objects.create_user(username, email, password)
            return render(request, "signin.html")
    return render(request, "signup.html")

def signin(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/api/add_recipe/')
        else:
            return render(request, "signup.html")
    return render(request, "signin.html")

def signout(request):
    logout(request)
    return redirect('/')

@login_required
def add_recipe(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        ingredients = request.POST.get('ingredients')
        ingredients=ingredients.replace(",","<br>")
        instructions = request.POST.get('instructions')
        notes = request.POST.get('notes')
        total_time =request.POST.get('total_time') 
        print(total_time)
        response_data = {}

        recipe = Recipe(title=title, ingredients=ingredients, instructions=instructions, notes=notes, total_time=total_time)
        recipe.save()

        response_data['result'] = 'Recipe added successful!'
        response_data['title'] = recipe.title
        response_data['ingredients'] = recipe.ingredients
        response_data['instructions'] = recipe.instructions
        response_data['notes'] = recipe.notes
        response_data['total_time'] = recipe.total_time

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return render(request, "add_recipe.html")

@login_required
def update_recipe(request, title):
    recipe=Recipe.objects.get(title=title)
    print(recipe)
    if request.method == 'POST':
        title = request.POST.get('title')
        ingredients = request.POST.get('ingredients')
        instructions = request.POST.get('instructions')
        notes = request.POST.get('notes')
        total_time =request.POST.get('total_time') 
        recipe.title=title
        recipe.ingredients=ingredients
        recipe.instructions=instructions
        recipe.notes=notes
        recipe.total_time=total_time
        recipe.save()
        response_data = {}
        response_data['result'] = 'Recipe added successful!'
        response_data['title'] = recipe.title
        response_data['ingredients'] = recipe.ingredients
        response_data['instructions'] = recipe.instructions
        response_data['notes'] = recipe.notes
        response_data['total_time'] = recipe.total_time

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return render(request, "update.html", {"recipe":recipe})


@login_required
def recipes(request): 
    recipes = Recipe.objects.all() # this is a queryset we should convert it into json. 
    # #manually construct a json
    payload = []
    for recipe in recipes:
        payload.append({"title": recipe.title, "ingredients": recipe.ingredients, "instructions": recipe.instructions, "notes": recipe.notes, "total_time": recipe.total_time})
    #converting dictionary to asci encoded ie json string
    payload = json.dumps(payload)
    return HttpResponse(payload, content_type="application/json")

@login_required    
def recipe_list(request):
    return render(request, "recipes.html")

# def timer(request):
#     return render(request, "timer.html", )


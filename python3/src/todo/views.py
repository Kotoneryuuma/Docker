from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import Todo

# Create your views here.

def index(request):
    all_todo_items = Todo.objects.all()
    return render(request, "todo/index.html", {'all_todo' : all_todo_items})



def add(request):
    todo = request.POST['title']
    time = request.POST['remind_at']
    new_todo = Todo( title = todo, remind_at = time )
    new_todo.save()
    return redirect("/")

def delete(request, idr):
    instance = Todo.objects.get(todo_id=idr)
    instance.delete()
    return redirect("/")

def edit(request,idr):
    context = {
        "todo": Todo.objects.get(todo_id=idr),
    }
    return render(request, "todo/edit.html", context)

def edit_process(request,idr):
    a_title = request.POST["title"]
    a_remind_at = request.POST["remind_at"]
    a_created_at = request.POST["created_at"]
    id = request.POST["whatever"]
    print(request.POST)
    ####### need to update ########
    editing=Todo.objects.get(todo_id=id)
    editing.title = a_title
    editing.remind_at = a_remind_at
    # editing.created_at = a_created_at
    editing.save()
    print(editing.title)
    return redirect("/")
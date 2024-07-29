from django.shortcuts import render,redirect
from .models import Todo,Profile

def home(request):
    return render(request, "home.html")


def todo(request):
    
    todos = Todo.objects.filter(is_completed = False)
    
    
    task_count = todos.count()
    parameters = {
        "todos" : todos,'task_count': task_count,    }
    return render(request, "todo.html", parameters)

 

def add_todo(request):
    
    if request.method == "POST":
        user_task = request.POST.get("task")
        user_priority = request.POST.get("priority")
        
        new_todo = Todo(task=user_task, priority=user_priority,is_completed=False)
        new_todo.save()
        
        return redirect("todo")
    
    return render(request, "add_todo.html")


def remove_todo(request, todo_id):
    
    todo = Todo.objects.get(id = todo_id)
    todo.delete()

    return redirect("todo")



def update_todo(request, todo_id):
    
    todo = Todo.objects.get(id = todo_id)
    
    if request.method == "POST":
        user_task = request.POST.get("task")
        user_priority = request.POST.get("priority")
        
        todo.task = user_task
        todo.priority = user_priority
        
        todo.save()
        
        return redirect("todo")
    
    parameters = {
        'todo': todo
    }
    
    return render(request, "update_todo.html", parameters)
 
def mark_complete(request,todo_id):
     todo = Todo.objects.get(id = todo_id)
     
     todo.is_completed = True
     todo.save()
     return redirect("todo")
 
 
 
def upload_profile(request):
    
    if request.method == "POST":
        profile_pic = request.FILES["profile_pic"]
        
        new_profile = Profile(title="demo title",profile_pic = profile_pic)
        
        new_profile.save()
        
        return redirect("todo")
    
    return render(request, "upload_profile.html")    
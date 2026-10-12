from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo

def todo_list(request):
    if request.method == "POST":
        if "add_task" in request.POST:
            title = request.POST.get("title", "").strip()
            if title:
                Todo.objects.create(title=title)
            return redirect("todo_list")

        if "edit_task" in request.POST:
            task_id = request.POST.get("task_id")
            new_title = request.POST.get("new_title", "").strip()
            todo = get_object_or_404(Todo, id=task_id)
            if new_title:
                todo.title = new_title
                todo.save()
            return redirect("todo_list")

        if "delete_task" in request.POST:
            task_id = request.POST.get("task_id")
            get_object_or_404(Todo, id=task_id).delete()
            return redirect("todo_list")

        if "clear_all" in request.POST:
            Todo.objects.all().delete()
            return redirect("todo_list")

    todos = Todo.objects.all().order_by("-created_at")
    return render(request, "todo/list.html", {
        "todos": todos,
        "task_count": todos.count(),
    })

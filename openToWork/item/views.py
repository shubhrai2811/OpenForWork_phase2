from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

from .models import Project  # Import the Project model from your app
from .forms import EditProjectForm  # Import the EditProjectForm from your forms module


from .forms import  EditItemForm
from .models import Category, Item
from .models import Item,Project

def detail(request,pk):
    item = get_object_or_404(Item ,pk=pk)
    related_items = Item.objects.filter(category=item.category).exclude(pk=pk)[0:3]

    return render(request,'item/detail.html',{
        'item':item ,
        'related_items' :related_items
        })


# def project_detail(request, pk):
#     project = get_object_or_404(Project, pk=pk)
#     related_projects = Project.objects.filter(category=project.category).exclude(pk=pk)[:3]

#     return render(request, 'item/project.html', {
#         'project': project,
#         'related_projects': related_projects
#     })
@login_required
def edit(request, pk):
    item = get_object_or_404(Item, pk=pk)

    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            form.save()

            return redirect('item:detail', pk=item.id)
    else:
        form = EditItemForm(instance=item)

    return render(request, 'item/form.html', {
        'form': form,
        'title': 'Edit item',
    })


@login_required
def edit_project(request, pk):
    project = get_object_or_404(Project, pk=pk)

    if request.method == 'POST':
        form = EditProjectForm(request.POST, request.FILES, instance=project)

        if form.is_valid():
            form.save()

            return redirect('project:detail', pk=project.pk)  # Replace 'project:detail' with the actual URL name for your project detail view
    else:
        form = EditProjectForm(instance=project)

    return render(request, 'item/project.html', {
        'form': form,
        'title': 'Edit Project',
    })
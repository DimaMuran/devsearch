from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm
from django.contrib.auth.decorators import login_required

#Search Project
def search(request):
    text = request.GET['text']
    data = Project.objects.filter(title__icontains=text)
    context = {'data':data}
    return render(request,'projects/search.html',context)

def projects(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    context = {'project':projectObj}
    return render(request, 'projects/single-project.html',context)


@login_required(login_url='login')
def createProject(request):
    form = ProjectForm()
    
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.owner = request.user
            form.save()
            return redirect('projects')

    context = {'form':form}
    return render(request, 'projects/project-form.html',context)


@login_required(login_url='login')
def updateProject(request, pk):
    project = Project.objects.get(id=pk)
    user = project.owner
    if user == request.user:
        form = ProjectForm(instance=project)

        if request.method == 'POST':
            form = ProjectForm(request.POST, request.FILES ,instance=project)
            if form.is_valid():
                form.save()
                return redirect('projects')

        context = {'form':form}

        return render(request, 'projects/project-form.html',context)
    return redirect('projects')


@login_required(login_url='login')
def deletePorject(request,pk):
    project = Project.objects.get(id=pk)
    user = project.owner
    if user == request.user:       
        if request.method == 'POST':
            project.delete()
            return redirect('projects')
        return render(request,'projects/delete.html', {'object':project})
    return redirect('projects')

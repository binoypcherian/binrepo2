from django.shortcuts import render, redirect
from .models import ToDo
from .forms import ToDoForm

# Create your views here.
def add(request):
    tasks = ToDo.objects.all
    if request.method=='POST':
        newname=request.POST.get('task')
        newprio=int(request.POST.get('priority'))
        newalarm=bool(request.POST.get('alarm'))
        if newalarm==1:
            newtime=request.POST.get('time')
            todonew = ToDo(taskname=newname, taskprio=newprio, taskalarm=newalarm, tasktime=newtime)
        elif newalarm==0:
            todonew = ToDo(taskname=newname, taskprio=newprio, taskalarm=newalarm)
        todonew.save()
    return render(request, 'home.html',{'tasklist':tasks})

def done(request,taskid):
    task=ToDo.objects.get(id=taskid)
    if request.method=='POST':
        task.delete()
        return redirect ('/')
    return render (request,'done.html')

def edit(request,taskid):
    todomodeledit=ToDo.objects.get(id=taskid)
    todoformedit=ToDoForm(request.POST or None, instance=todomodeledit)
    if todoformedit.is_valid():
        todoformedit.save()
        return redirect('/')
    return render (request,'edit.html',{'todoform':todoformedit,'todomodel':todomodeledit})





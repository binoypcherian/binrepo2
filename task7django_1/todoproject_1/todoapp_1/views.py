from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from .models import ToDo
from django.urls import reverse_lazy

# Create your views here.
def add(request):
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
    return render(request, 'home.html')

class cgvlist(ListView):
    model=ToDo
    template_name='list.html'
    context_object_name='tasklist'

class cgvdetail(DetailView):
    model=ToDo
    template_name='details.html'
    context_object_name='taskdetail'

class cgvupdate(UpdateView):
    model=ToDo
    template_name='update.html'
    context_object_name='taskupdate'
    fields=('taskname','taskprio','taskalarm','tasktime')
    def get_success_url(self):
        return reverse_lazy ('details',kwargs={'pk':self.object.id})

class cgvdelete(DeleteView):
    model=ToDo
    template_name='delete.html'
    success_url=reverse_lazy('list')

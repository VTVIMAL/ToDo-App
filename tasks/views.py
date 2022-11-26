from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView, 
    UpdateView, 
    DeleteView
    )
from django.urls import reverse_lazy


from .models import Task
# Create your views here.

class TaskLists(ListView):
    '''Display all the user tasks'''
    model = Task
    context_object_name = 'tasks'
    template_name = "task_list.html"
    ordering = ["-date_created"] # order the list by the date created

class TaskDetail(DetailView):
    '''Display all the individulal tasks'''
    model = Task
    template_name ="task_detail.html"

class TaskCreate(CreateView):
    '''Create a new Task'''
    model = Task
    fields = ("title", "discription",)
    template_name = "task_create.html"

    def form_valid(self, form): # only validate the form if the author and the current user are the same
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class TaskUpdate(UpdateView):
    '''Edit an existing task'''
    model = Task
    fields= ("title", "discription", "completed", )
    template_name = "task_update.html"
    

class TaskDelete(DeleteView):
    '''Delete the selected task'''
    model = Task
    template_name= "task_delete.html"
    success_url = reverse_lazy("home") # return to home page after succesful deletion
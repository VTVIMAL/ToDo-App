from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView, 
    UpdateView, 
    DeleteView
    )
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy


from .models import Task
# Create your views here.

class TaskLists(LoginRequiredMixin, ListView):
    '''Display all the user tasks'''
    model = Task
    context_object_name = 'tasks'
    template_name = "task_list.html"
    ordering = ["-date_created"] # order the list by the date created

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # show tasks created by the current user only
        context['tasks'] = context['tasks'].filter(author = self.request.user)
        # count the total number of incomplete tasks
        context['count'] = context['tasks'].filter(completed=False).count()
        # search filtering
        search_input = self.request.GET.get("search-area") or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(title__startswith=search_input)
        context['search_input'] = search_input
        # count total tasks incomplete and complete 
        task_count = context['tasks'].count()
        context['task_count'] = task_count
        return context

class TaskDetail(LoginRequiredMixin, UserPassesTestMixin,  DetailView):
    '''Display all the individulal tasks'''
    model = Task
    template_name ="task_detail.html"

    def test_func(self):
        # test if author of the task is the user requesting access
        task = self.get_object()
        return task.author == self.request.user

class TaskCreate(LoginRequiredMixin, CreateView):
    '''Create a new Task'''
    model = Task
    fields = ("title", "discription",)
    template_name = "task_create.html"

    def form_valid(self, form): # only validate the form if the author and the current user are the same
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class TaskUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    '''Edit an existing task'''
    model = Task
    fields= ("title", "discription", "completed", )
    template_name = "task_update.html"
    
    def test_func(self):
        task = self.get_object()
        return task.author == self.request.user

class TaskDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    '''Delete the selected task'''
    model = Task
    template_name= "task_delete.html"
    success_url = reverse_lazy("home") # return to home page after succesful deletion

    def test_func(self):
        task = self.get_object()
        return task.author == self.request.user
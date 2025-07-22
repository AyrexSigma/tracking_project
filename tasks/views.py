from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Task
from .forms import TaskForm
from django.views.generic import TemplateView
from django.http import HttpResponse

# Create your views here.

class HomeView(TemplateView):
    template_name = 'home.html'


class TaskListView(ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'

class TaskDetailView(DetailView):
    model = Task
    template_name = 'tasks/task_detail.html'

class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_form.html'
    success_url = '/tasks/'
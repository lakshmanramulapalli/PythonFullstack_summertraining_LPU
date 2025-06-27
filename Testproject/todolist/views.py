from django.shortcuts import render
from django.views import generic

from todolist.models import Todo


# Create your views here.
class TodoListView(generic.ListView):
    model = Todo
    template_name = 'list.html'


class TodoCreateView(generic.CreateView):
    model = Todo
    template_name = 'create.html'
    fields = ['title', 'description', 'is_active']

class TodoUpdateView(generic.UpdateView):
    model = Todo
    template_name = 'update.html'
    fields = ['title', 'description', 'is_active']

class TodoDeleteView(generic.DeleteView):
    model = Todo
    template_name = 'delete.html'



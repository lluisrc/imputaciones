from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Registro
from django.views.generic import ListView, DetailView

def index(request):
    return render(request, 'index.html')


class RegistroListView(ListView):
    model = Registro
    def get_queryset(self):
        return Registro.objects.order_by('dia')


class RegistroDetailView(DetailView):
    model = Registro


class RegistroCreate(CreateView):
    model = Registro
    fields = '__all__'

class RegistroUpdateView(UpdateView):
    model = Registro
    fields = ['dia','entrada','comida','llegada','salida']
    template_name_suffix = '_update_form'


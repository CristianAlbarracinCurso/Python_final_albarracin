# views.py
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import Page

# Vistas basadas en funciones

def home(request):
    return render(request, 'blog/home.html')

def about(request):
    return render(request, 'blog/about.html')

def contact(request):
    return render(request, 'contact.html')

def services(request):
    return render(request, 'services.html')

def posts(request):
    return render(request, 'blog/posts.html')

def profile(request):
    return render(request, 'profile.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Credenciales inválidas'})
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

# Vistas basadas en clases para el modelo Page

class PageListView(ListView):
    model = Page
    template_name = 'pages_list.html'  # Asegúrate de que esta plantilla exista

class PageDetailView(DetailView):
    model = Page
    template_name = 'page_detail.html'  # Asegúrate de que esta plantilla exista

class PageCreateView(CreateView):
    model = Page
    fields = ['title', 'subtitle', 'content', 'image']
    template_name = 'page_form.html'  # Asegúrate de que esta plantilla exista
    success_url = '/pages/'

class PageUpdateView(UpdateView):
    model = Page
    fields = ['title', 'subtitle', 'content', 'image']
    template_name = 'page_form.html'  # Asegúrate de que esta plantilla exista
    success_url = '/pages/'

class PageDeleteView(DeleteView):
    model = Page
    template_name = 'page_confirm_delete.html'  # Asegúrate de que esta plantilla exista
    success_url = '/pages/'
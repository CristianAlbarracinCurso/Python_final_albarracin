from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Page
from django.shortcuts import render

def home(request):
    return render(request, 'blog/home.html')  

class PageListView(ListView):
    model = Page
    template_name = 'blog/pages_list.html'

class PageDetailView(DetailView):
    model = Page
    template_name = 'blog/page_detail.html'

class PageCreateView(LoginRequiredMixin, CreateView):
    model = Page
    fields = ['title', 'subtitle', 'content', 'image']

class PageUpdateView(LoginRequiredMixin, UpdateView):
    model = Page
    fields = ['title', 'subtitle', 'content', 'image']

class PageDeleteView(LoginRequiredMixin, DeleteView):
    model = Page
    success_url = '/'
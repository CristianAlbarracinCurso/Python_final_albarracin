from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import PageForm
from .models import Page
from accounts.forms import CustomUserCreationForm, EditProfileForm


# Vistas basadas en funciones

def home(request):
    posts = Page.objects.all().order_by('-created_at')  # Posts ordenados por fecha
    return render(request, 'blog/home.html', {'posts': posts})


@login_required
def page_create(request):
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            page = Page(title=title, content=content)  
            page.save()
            messages.success(request, "¡El post se ha creado correctamente!")
            return redirect('home')  # Redirige después de guardar
    else:
        form = PageForm()
    return render(request, 'page_create.html', {'form': form})

@login_required
def page_edit(request, post_id):
    post = get_object_or_404(Page, id=post_id, author=request.user)  # Solo el autor puede editar
    if request.method == 'POST':
        form = PageForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Post actualizado exitosamente!')
            return redirect('home')
    else:
        form = PageForm(instance=post)
    return render(request, 'blog/page_edit.html', {'form': form})


@login_required
def page_cenfirm_delete(request, post_id):
    post = get_object_or_404(Page, id=post_id, author=request.user)  # Solo el autor puede borrar
    if request.method == 'POST':
        post.delete()
        messages.success(request, '¡Post eliminado exitosamente!')
        return redirect('home')
    return render(request, 'blog/page_confirm_delete.html', {'post': post})


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def contact_submit(request):
    if request.method == 'POST':
        messages.success(request, "¡Gracias, tu mensaje ha sido enviado con éxito!")
        return redirect('home')
    return HttpResponse("Método no permitido", status=405)


@login_required
def profile(request):
    return render(request, 'accounts/profile.html', {'user': request.user})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Perfil actualizado exitosamente.')
            return redirect('profile')
    else:
        form = EditProfileForm(instance=request.user)
    return render(request, 'accounts/edit_profile.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user, backend='allauth.account.auth_backends.AuthenticationBackend')
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')


# Vistas basadas en clases para el modelo Page
class PageListView(ListView):
    model = Page
    template_name = 'blog/pages_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Page.objects.filter(author=self.request.user).order_by('-created_at')


class PageDetailView(DetailView):
    model = Page
    template_name = 'blog/page_detail.html'


class PageCreateView(CreateView):
    model = Page
    fields = ['title', 'subtitle', 'content', 'image']
    template_name = 'blog/page_create.html'
    success_url = '/pages/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PageUpdateView(UpdateView):
    model = Page
    fields = ['title', 'subtitle', 'content', 'image']
    template_name = 'blog/page_edit.html'
    success_url = '/pages/'


class PageDeleteView(DeleteView):
    model = Page
    template_name = 'blog/page_confirm_delete.html'
    success_url = '/pages/'

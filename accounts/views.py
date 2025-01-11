# accounts/views.py
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin  # Importa LoginRequiredMixin
from .forms import CustomUserCreationForm
from .forms import EditProfileForm



class LoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'accounts/login.html', {'form': form})

    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home')  # Redirige a la página de inicio después de login
        return render(request, 'accounts/login.html', {'form': form})

class SignupView(View):
    def get(self, request):
        form = CustomUserCreationForm()  # Usa el formulario de usuario personalizado
        return render(request, 'accounts/signup.html', {'form': form})

    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Guarda el nuevo usuario
            login(request, user)  # Inicia sesión automáticamente después del registro
            return redirect('edit_profile')  # Redirige a la página de inicio después del registro
        return render(request, 'accounts/signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

# Usa LoginRequiredMixin en lugar de @login_required
class EditProfileView(LoginRequiredMixin, View):
    def get(self, request):
        form = EditProfileForm(instance=request.user)  # Pasa la instancia del usuario actual al formulario
        return render(request, 'accounts/edit_profile.html', {'form': form})

    def post(self, request):
        form = EditProfileForm(request.POST, request.FILES, instance=request.user)  # Incluye archivos para campos como 'avatar'
        if form.is_valid():
            form.save()  # Guarda los cambios del perfil
            return redirect('profile')  # Redirige a la página de perfil después de actualizar
        return render(request, 'accounts/edit_profile.html', {'form': form})  # Renderiza el formulario con errores si los hay
    pass

# accounts/views.py
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin  # Importa LoginRequiredMixin
from .forms import CustomUserCreationForm

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
            return redirect('home')  # Redirige a la página de inicio después del registro
        return render(request, 'accounts/signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

# Usa LoginRequiredMixin en lugar de @login_required
class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'accounts/profile.html')  # Asegúrate de crear esta plantilla

class EditProfileView(LoginRequiredMixin, View):
    def get(self, request):
        # Aquí puedes usar un formulario para editar el perfil
        return render(request, 'accounts/edit_profile.html')  # Asegúrate de crear esta plantilla

    def post(self, request):
        # Aquí puedes manejar la lógica de actualización del perfil
        pass

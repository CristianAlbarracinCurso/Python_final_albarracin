from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin  
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
        form = CustomUserCreationForm()  
        return render(request, 'accounts/signup.html', {'form': form})

    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save() 
            login(request, user)  
            return redirect('edit_profile')  
        return render(request, 'accounts/signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

class EditProfileView(LoginRequiredMixin, View):
    def get(self, request):
        form = EditProfileForm(instance=request.user)  
        return render(request, 'accounts/edit_profile.html', {'form': form})

    def post(self, request):
        form = EditProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()  
            return redirect('profile')  
        return render(request, 'accounts/edit_profile.html', {'form': form})  
    pass

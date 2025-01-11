from django.urls import path
from . import views
from django.contrib.auth.views import PasswordChangeView

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('profile/edit/', views.EditProfileView.as_view(), name='edit_profile'),
    path('password-change/', PasswordChangeView.as_view(template_name='accounts/password_change.html'), name='password_change'),
]
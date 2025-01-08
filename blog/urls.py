# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services'),
    path('posts/', views.posts, name='posts'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.login_view, name='login'),  # Cambié a login_view
    path('register/', views.register, name='register'),
    
    # Vistas basadas en clases para el modelo Page
    path('pages/', views.PageListView.as_view(), name='pages_list'),
    path('pages/<int:pk>/', views.PageDetailView.as_view(), name='page_detail'),
    path('pages/create/', views.PageCreateView.as_view(), name='page_create'),
    path('pages/<int:pk>/update/', views.PageUpdateView.as_view(), name='page_update'),
    path('pages/<int:pk>/delete/', views.PageDeleteView.as_view(), name='page_delete'),
]
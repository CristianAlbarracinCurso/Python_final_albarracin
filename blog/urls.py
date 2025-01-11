from django.urls import path
from . import views

urlpatterns = [
    # Home
    path('', views.home, name='home'),

    # Posts
    path('post/create/', views.page_create, name='page_create'),
    path('post/edit/<int:post_id>/', views.page_edit, name='page_edit'),
    path('post/delete/<int:post_id>/', views.page_cenfirm_delete, name='page_cenfirm_delete'),

    # About and Contact
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('contact/submit/', views.contact_submit, name='contact_submit'),

    # User Profile
    path('profile/', views.profile, name='profile'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),  

    # Authentication
    path('login/', views.login_view, name='login'),
    path('signup/', views.register, name='signup'),
    path('logout/', views.logout_view, name='logout'),

    # Pages (CBV)
    path('pages/', views.PageListView.as_view(), name='pages_list'),
    path('pages/<int:pk>/', views.PageDetailView.as_view(), name='page_detail'),
    path('pages/create/', views.PageCreateView.as_view(), name='page_create'),
    path('pages/<int:pk>/update/', views.PageUpdateView.as_view(), name='page_update'),
    path('pages/<int:pk>/delete/', views.PageDeleteView.as_view(), name='page_delete'),
]

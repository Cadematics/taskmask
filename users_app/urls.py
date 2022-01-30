from django.urls import path
from users_app import views as users_app_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register', users_app_views.register, name = 'register_page'),
    path('login', auth_views.LoginView.as_view(template_name='login.html'), name = 'login_page'),
    path('logout', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout_page'),
]

from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='dashboard/login.html'), name='login'),
    path('home/', views.dashboard_home, name='dashboard_home'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # bu qatorni qo‘shing
]

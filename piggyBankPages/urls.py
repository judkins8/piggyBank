from django.urls import path
from .views import piggyBankPagesView, parent_dashboard
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", piggyBankPagesView, name="index"),
    path('parent_dashboard/', parent_dashboard, name='parent_dashboard'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]             
"""
URL configuration for demo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from userapp import views
from userapp.views import about

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login',views.login_view),
    path('',views.home),
    path('login',views.register),
    path('organizer_dashboard/', views.organizer_dashboard, name='organizer_dashboard'),
    path('tournament',views.tournament),
    path('tournament_details/<int:id>',views.view_tournament),
    path('book_add',views.add_book),
    path('tournament_register/<int:id>', views.register_tournament),
    path('login', views.login_view, name="login"),
    path('user_dashboard', views.user_dashboard, name="user_dashboard"),
    path('logout', views.logout_view, name="logout"),
    path('about',views.about),
    path('contact',views.contact),
    path('my_dashboard',views.my_dashboard),
    path('register',views.register),
    path('update_tournament/<int:tournament_id>/', views.update_tournament, name='update_tournament'),
    path('delete_tournament/<int:tournament_id>/', views.delete_tournament, name='delete_tournament'),
    path('delete_registration/<int:registration_id>/', views.delete_registration, name='delete_registration'),
]





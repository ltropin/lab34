from django.urls import path
from clubbing import views


urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register_page, name='register'),
    path('logout/', views.logout_page, name='logout'),
    path('login/', views.login_page, name='login'),
]
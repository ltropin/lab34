from django.urls import path
from clubbing import views


urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register_page, name='register'),
    path('logout/', views.logout_page, name='logout'),
    path('login/', views.login_page, name='login'),
    path('purchases/', views.purchases, name='purchases'),
    path('clubbings/', views.clubbings, name='clubbings'),
    path('add-purchase/', views.add_purchase, name='add_purchase'),
    path('item/<pk>/', views.detail_item),
    # path('club/<pk>/', views.detail_club),
]
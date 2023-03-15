from django.urls import path
from . import views
urlpatterns = [
    path('', views.Home, name='Home'),
    # path('/', views.Home, name='Home1'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),

    # path('mul/', views.multiplication, name='mul'),
    # path('div/', views.division, name='div')

]
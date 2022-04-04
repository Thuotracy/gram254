# from django.urls import path
from account.views import landing, search_results, home_view,register, login_view, logout_view, Post


urlpatterns=[
  path('', landing, name='home'),
  path('search/', search_results, name='search_results'),
  path('dashboard/', home_view, name='dashboard'),
  path('dashboard/', Post.as_view(), name='dashboard'),
  path('register/', register, name='register'),
  path('login/', login_view, name='login'),
  path('logout/', logout_view, name='logout'),
]
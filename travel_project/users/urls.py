from django.urls import path
from .views import *

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('profile/', profile, name='profile'),
    # path('logged-out/', logged_out_view, name='logged-out'),  # 🔹 New URL for Logged Out Page
]
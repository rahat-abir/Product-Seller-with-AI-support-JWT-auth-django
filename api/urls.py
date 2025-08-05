from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from . import views

app_name = 'api'

urlpatterns = [
    path('register/', views.register_api, name='register'),
    path('login/', views.login_api, name='login'),
    path('profile/', views.user_profile_api, name='profile'),
    path('logout/', views.logout_api, name='logout'),
    path('products/', views.products_api, name='products'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
] 
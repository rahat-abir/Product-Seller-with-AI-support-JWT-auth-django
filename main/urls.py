from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('products/', views.products_view, name='products'),
    path('ask/', views.ask_view, name='contact_seller'),
    path('logout/', views.logout_view, name='logout'),
    path('chat/webhook/', views.chat_webhook, name='chat_webhook'),
] 
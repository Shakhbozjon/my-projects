from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import user_login, SignUpView

urlpatterns = [
    # path('login/', user_login, name='login')
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', SignUpView.as_view(), name='user_register')
]
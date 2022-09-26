from django.urls import path
from User.views import LoginView, LogoutView, RegisterView, ChangePasswordView
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='/login/', permanent=True)),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('home/change-password', ChangePasswordView.as_view(),
         name='change_password'),
]

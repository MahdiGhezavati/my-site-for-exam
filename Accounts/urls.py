from django.urls import path
from Accounts.views import *
from django.urls import path
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views

app_name = "Accounts"
urlpatterns = [
    path("login" , view_login, name="login"),
    path("logout" , view_logout ,name= "logout"),
    path("signup" , view_signup ,name= "signup"),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='Accounts/password_reset.html',
                                                                  success_url=reverse_lazy('Accounts:password_reset_done'),
                                                                  email_template_name = "Accounts/password_reset_email.html",
                                                                  html_email_template_name="Accounts/password_reset_email.html",
                                                                  ), 
                                                                    name="password_reset"),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='Accounts/password_reset_confirm.html' , success_url=reverse_lazy("Accounts:password_reset_complete")),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='Accounts/password_reset_complete.html'),
         name='password_reset_complete'),
    path('password-reset-done/',
         auth_views.PasswordResetDoneView.as_view(template_name='Accounts/password_reset_done.html'),
         name='password_reset_done'),
]

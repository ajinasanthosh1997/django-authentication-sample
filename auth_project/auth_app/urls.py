# auth_app/urls.py
from django.urls import path
from .views import signup, login_view,home,logout_view,forgot_password
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
    path('', home, name='home'),  # Add this line
    path('logout/', logout_view, name='logout'),  # Add this line
    path('forgot-password/', auth_views.PasswordResetView.as_view(
        template_name='forgot_password.html',  # Custom template for password reset form
        email_template_name='password_reset_email.html',  # Custom template for password reset email
        subject_template_name='password_reset_subject.txt',  # Custom email subject template
    ), name='forgot_password'),

    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]

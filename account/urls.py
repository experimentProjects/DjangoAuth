from django.urls import path
from account.views import SendPasswordResetEmailView, UserChangePasswordView, UserPasswordResetView, UserProfileView, UserRegistrationView, UserLoginView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name="register"),
    path('login/', UserLoginView.as_view(), name="login"),
    path('profile/', UserProfileView.as_view(), name="user profile"),
    path('changepassword/', UserChangePasswordView.as_view(), name="change password"),
    path('send-reset-password-email/', SendPasswordResetEmailView.as_view(),
         name="send password reset email"),
    path('reset-password/<uid>/<token>/',
         UserPasswordResetView.as_view(), name="reset password")
]

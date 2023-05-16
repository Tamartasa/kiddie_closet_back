from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from kiddie_closet_app.views.users import sign_up, get_user_data, get_all_users, google_auth

urlpatterns = [
    path('signup/', sign_up),
    path('data/', get_user_data),
    path('users/', get_all_users),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('token/google/', google_auth)
    ]
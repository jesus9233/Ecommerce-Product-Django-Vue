from django.urls import path
from .views import login, is_auth, UserRegisterView

app_name = 'user'


urlpatterns = [
    path('login/', login),
    path('register/', UserRegisterView.as_view()),
    path('is_auth/', is_auth)
]

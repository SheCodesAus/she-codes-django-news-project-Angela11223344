from django.urls import path
from .views import CreateAccountView, EditAccountView, ProfileView

app_name = 'users'

urlpatterns = [
    path('create-account/', CreateAccountView.as_view(), name='createAccount'),
    path('<int:pk>/view-profile', ProfileView.as_view(), name='viewAccount'),
    path('<int:pk>/edit-profile', EditAccountView.as_view(), name='editAccount'),
]
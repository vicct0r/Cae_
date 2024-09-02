from django.urls import path
from .views import IndexView, MyAccountUpdateView, MyProfileUpdateView, MyProfileView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('profile/<int:pk>/', MyProfileView.as_view(), name='my_profile'),
    path('profile/<int:pk>/edit_profile/', MyProfileUpdateView.as_view(), name='my_profile_update'),
    path('profile/<int:pk>/edit_account/', MyAccountUpdateView.as_view(), name='my_account_update'),
]
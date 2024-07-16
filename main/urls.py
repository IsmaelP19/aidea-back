from django.urls import path
from .views import UserInfoView, UserListCreateView

urlpatterns = [
    path('users/', UserListCreateView.as_view(), name='users'),
    path('users/<int:pk>/', UserInfoView.as_view(), name='user'),

]

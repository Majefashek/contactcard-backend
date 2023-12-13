
from django.urls import path, include
from .views import LoginAPIEndpoint, SignUpAPIEndpoint, RetrieveUserEndpoint, UpdateUserInfoEndpoint,DeleteUserInfo

urlpatterns = [
    path('login/',LoginAPIEndpoint.as_view(), name="login"),
    path('signup/',SignUpAPIEndpoint.as_view(), name="signup"),
    path('retrieve/',RetrieveUserEndpoint.as_view(), name="retrieve_user"),
    path('update/<int:pk>',UpdateUserInfoEndpoint.as_view(), name="update_info"),
    path('delete/<int:pk>',DeleteUserInfo.as_view(), name="delete_user"),
]
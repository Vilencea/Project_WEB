from django.urls import path
from .views import LoginV, LogoutVV, RegisterV

urlpatterns = [
    path('login/',LoginV.as_view(), name='login'),
    path('logout/', LogoutVV.as_view(), name='logout'),
    path('register/', RegisterV.as_view(), name='register')
]

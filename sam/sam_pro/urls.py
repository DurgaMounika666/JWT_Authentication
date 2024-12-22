from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

from .views import *
from rest_framework.authtoken.views import obtain_auth_token




urlpatterns=[
    path('create/',Create,name='Create'),
    path('all/',All,name='All'),
    path('update/<int:id>/',Update,name='Update'),
    path('delete/<int:id>/',Delete,name='Delete'),
    path('userlogin/',login_view,name='UserLogin'),

    path('logout/',logout_view,name='UserLogout'),


    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),



]

from django.urls import path
from . import views

urlpatterns = [
    path('user/login', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/register', views.userRegistration, name="userRegister"),
    path('users/profile', views.getUserProfile, name="userProfile"),
    path('users/profile/update', views.getUserProfileUpdate, name="userProfileUpdate"),
    path('users/', views.getUsers, name="users"),
    path('products/', views.getProducts, name="products"),
    path('products/<str:pk>', views.getProduct, name="product"),
]

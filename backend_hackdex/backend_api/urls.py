from django.urls import path
from .views import CategoriesWithSubcategoriesAndAttacks,AttackContentAPI,HomePageAPI,MyTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView
urlpatterns = [
    path("categoriesWhithOthers",CategoriesWithSubcategoriesAndAttacks.as_view(),name="CategoriesWithOthers"),
    path("getContentAttack/",AttackContentAPI.as_view(),name="AttackContentAPI"),
    path("getHomePage",HomePageAPI.as_view(),name="HomePageAPI"),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),

    
]

   
    
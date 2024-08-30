from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import get_user_model
from .serializers import CustomTokenObtainPairSerializer
user=get_user_model()



class CustomTokenObtainPairView(TokenObtainPairView):
    def get_token(cls, user):
        token = super().get_token(user)
        
        
        token['type_account_name'] = user.type_account
        print(user.type_account)
        
        
        return token
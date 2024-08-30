from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import status
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from .regex import *
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import AuthenticationFailed




User = get_user_model()


class CreateAccount(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        password2=request.data.get('password2')
        email= request.data.get('email')
        dateofbirth=request.data.get('dateofbirth')
        isValidData:bool=(validate_email(email) and validate_password(password) and validate_username(username) 
                          and validate_password2(password,password2))
        if not isValidData:
            return Response({'message': 'Erreurs de champs'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            user = User.objects.create_user(username=username, password=password, email=email)
            user.date_of_birth = dateofbirth
            user.save()
            response=Response({'message': 'Utilisateur créé avec succès.'}, status=status.HTTP_201_CREATED)
            response['Access-Control-Allow-Origin']="http://localhost:3000"
            return response
        except Exception as e:
            response=Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)
            response['Access-Control-Allow-Origin']="http://localhost:3000"

            return response
     
class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        print(email,password)
        user = authenticate(email=email, password=password)
       
        if user is not None:
            serializer = CustomTokenObtainPairSerializer(data={"email": email, "password": password})
            serializer.is_valid(raise_exception=True)
            token = serializer.validated_data['access']
            print(token)
            
            response = Response({
                'access': token,
                #'type_account_name': token['type_account_name'],  # Revendication personnalisée: nom du type de compte
                #'type_account_description': token['type_account_description'],  # Revendication personnalisée: description du type de compte
            }, status=status.HTTP_200_OK)
            response['Access-Control-Allow-Origin'] = "http://localhost:3000"
            print("duanal")
            return response
        else:
            error_response = {'error': 'Nom d\'utilisateur ou mot de passe incorrect'}
            error_response['Access-Control-Allow-Origin'] = "http://localhost:3000"
            return Response(error_response, status=status.HTTP_400_BAD_REQUEST)
        
class CustomJWTAuthentication(JWTAuthentication):
    def authenticate(self, request):
        # Appeler la méthode authenticate de la classe parente pour obtenir l'utilisateur et le jeton
        user, token = super().authenticate(request)

        # Vérifier si l'utilisateur est actif et son compte n'a pas expiré
        if user is not None and not user.is_active:
            raise AuthenticationFailed('User account is inactive.')
        # Vérifier si le compte de l'utilisateur a expiré (par exemple, si la date d'expiration est dépassée)
        if user is not None and user.account_expiration_date is not None and user.account_expiration_date < timezone.now():
            raise AuthenticationFailed('User account has expired.')

        # Retourner l'utilisateur et le jeton
        return user, token
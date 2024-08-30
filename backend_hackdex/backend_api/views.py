from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.views import TokenObtainPairView




    

class CategoriesWithSubcategoriesAndAttacks(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        response=Response(serializer.data)
        response["Access-Control-Allow-Origin"] = "http://localhost:3000"
        return response



class AttackContentAPI(APIView):
    def get(self,request):
        pk = request.GET.get('id')
        attack=Attack.objects.get(id=pk)
        serializer=AttackContentSerializer(attack,many=False)
        response=Response(serializer.data)
        response["Access-Control-Allow-Origin"] = "http://localhost:3000"
        return response

class HomePageAPI(APIView):
    def get(self,request):
        home_page=IndividualPage.objects.get(name="Home Page")
        serializer= IndividualPageSerializer(home_page)
        response=Response(serializer.data)
        response["Access-Control-Allow-Origin"]="http://localhost:3000"
        return response


class MyTokenObtainPairView(TokenObtainPairView):

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
            token_pair = serializer.validated_data
            return Response({
                'access': str(token_pair.access_token),
                'refresh': str(token_pair.refresh_token),
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
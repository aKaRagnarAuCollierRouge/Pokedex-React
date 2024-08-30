from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Ajoutez vos revendications personnalisées au jeton ici
        token['type_account_name'] = user.type_account
        print(user.type_account)
      

        return token
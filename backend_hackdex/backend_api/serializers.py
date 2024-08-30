from rest_framework import serializers
from .models import *

#------API pour le contenu de la page





class AttackContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attack
        fields = ["id","name","difficult","description"]
    
    
    
#API pour la side Bare pour la liste déroulement

class AttackSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Attack
        fields = ["id","name","sub_category","difficult"]

class SubCategorySerializer(serializers.ModelSerializer):
    attacks = AttackSerializer(many=True)

    class Meta:
        model = SubCategory
        fields = ['name','attacks']

class CategorySerializer(serializers.ModelSerializer):
    subcategories = SubCategorySerializer(many=True)

    class Meta:
        model = Category
        fields = ['name', 'subcategories']


class IndividualPageSerializer(serializers.ModelSerializer):
    class Meta:
        model=IndividualPage
        fields=['name','content']




        


from django.db import models
from tinymce import models as tinymce_models
# Create your models here.


class IndividualPage(models.Model):
    name=models.CharField(max_length=100,primary_key=True)
    content=tinymce_models.HTMLField()
    def __str__(self):
        return self.name



class Category(models.Model):
    name = models.CharField(max_length=100,primary_key=True)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name=models.CharField(max_length=100,primary_key=True)
    category=models.ForeignKey(Category,on_delete=models.SET_NULL,related_name='subcategories', null=True, blank=True)
    def __str__(self):
        return self.name
    
class LevelDifficult(models.Model):
    levelDifficult=models.IntegerField(primary_key=True)
    nameDifficult=models.CharField(max_length=100)
    
    def __str__(self):
        return str(self.levelDifficult)




class Attack(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    sub_category=models.ForeignKey(SubCategory ,on_delete=models.SET_NULL,related_name='attacks', null=True, blank=True)
    description=tinymce_models.HTMLField()
    difficult=models.ForeignKey(LevelDifficult,blank=True,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.name


    




    
   

    



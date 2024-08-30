from django.shortcuts import render
from backend_api.models import Category,SubCategory,Attack
from django.views.generic import View
from django.http import HttpResponse
from django.template import loader

def create_context_adminpage():
    context = {"categories": {}}
    categories = Category.objects.all()
    for category in categories:
        category_name = category.name
        context["categories"][category_name] = {"subcategories": {}}
        
        subcategories = SubCategory.objects.filter(category=category)
        
        for subcategory in subcategories:
            subcategory_name = subcategory.name
            context["categories"][category_name]["subcategories"][subcategory_name] = {"attacks": Attack.objects.filter(sub_category=subcategory)}
                
    return context


class TreeModelView(View):
    def get(self, request, *args, **kwargs):
        context=create_context_adminpage()
        template = loader.get_template('tree-view-model.html')
        return HttpResponse(template.render(context, request))


from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include("backend_api.urls")),
    path('tinymce/', include('tinymce.urls')),
    path('manageModels/',include('manage_models.urls')),
    path('api-account/',include("account_api.urls"))

]
   


endpoint="http://127.0.0.1:8081/api"
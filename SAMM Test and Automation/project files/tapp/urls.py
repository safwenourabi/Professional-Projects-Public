from django.contrib import admin
from django.urls import path,include
from django.http import HttpResponse
from . import views
from tapp.models import ticket 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('main',views.main , name="main"),
    path('delete/<int:id>/',views.deletepost, name='delete_post'),
    path('treatpost/<int:id>' , views.treatpost ,name='treatpost'),
]
  
    

 
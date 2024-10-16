from django.urls import path
from appsecundaria import views
urlpatterns = [
   path("",views.Index.visual,name="Index.vista")
]
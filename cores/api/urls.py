from django.urls import path,include
from home.views import ReceipeAPI
urlpatterns = [
   
    path('receipes/', ReceipeAPI.as_view())
]

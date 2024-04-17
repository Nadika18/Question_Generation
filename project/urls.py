from django.urls import path,include
from .views import index,submitQ

urlpatterns = [
 path('',index,name='index'),
 path('submit-question',submitQ,name='submit-question'),
]
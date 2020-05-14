from django.urls import path
from . import views

urlpatterns = [
    path('api/common/',views.CommonListCreate.as_view() ),

]
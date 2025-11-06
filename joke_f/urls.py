from . import views
from django.urls import path

urlpatterns = [
    path('Fetch/', views.fetch_and_store_jokes,name="Fetch_and_store_jokes"),
    path('get_jokes/',views.get_jokes,name="Get_jokes"),
]

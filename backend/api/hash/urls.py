from django.urls import path
from .views import ListCreateHashesView, HashesDetailView

urlpatterns = [
    path('hashes/', ListCreateHashesView.as_view(), name="hashes-list-create"),
    path('hashes/<str:pk>/', HashesDetailView.as_view(), name="hashes-detail"),
]

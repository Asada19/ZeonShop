from django.urls import path 
from .views import CollectionAPIView, CollectionDetailAPIWiew, PerviosAPIVew, ProductAPIView


urlpatterns = [
    path('products/',ProductAPIView.as_view()),
    path('collections/', CollectionAPIView.as_view()),
    path('collections/<int:pk>/', CollectionDetailAPIWiew.as_view())
]


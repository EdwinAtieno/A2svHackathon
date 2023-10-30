from django.urls import path
from .views import RecommendationListCreateView, RecommendationDetailView

urlpatterns = [
    path('api/recommendations/', RecommendationListCreateView.as_view(), name='recommendation-list'),
    path('api/recommendations/<int:pk>/', RecommendationDetailView.as_view(), name='recommendation-detail'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.MovieCreateView.as_view()),
    path('all/', views.MovieListView.as_view()),
    path('<int:pk>/', views.MovieAPIView.as_view()),
    path('vote/<int:pk>', views.MovieVoteAPIView.as_view())
]

from django.urls import path
from. import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('results/', views.SearchView.as_view(), name='search'),
    path('api/news', views.NewsList.as_view(), name="news-list"),
    path('api/news/<int:pk>/', views.NewsDetail.as_view(), name="news-detail"),    
]
 
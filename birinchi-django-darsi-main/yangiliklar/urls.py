from django.urls import path, include
from .views import NewsListView, add_news, CategoryList, CategoryView, CategoryAPIView, CategoryDetail, Category2List


urlpatterns = [
    path("list/", NewsListView),
    path("add/", add_news),
    path("category/", CategoryList.as_view()),
    path("category/<int:id>/", CategoryView.as_view()),
    path("category/api/", CategoryAPIView.as_view()),
    
    
    path("category/list/", Category2List.as_view()),
    path("category/detail/<int:pk>/", CategoryDetail.as_view()),
]

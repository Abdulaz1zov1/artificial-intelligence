from django.urls import path
from .views import (book_view, author_view, category_view,
                    book_view_by_id)

urlpatterns = [
    path('list/', book_view),
    path('list/<int:id>/', book_view_by_id),
    path('authors/', author_view),
    path('categories/', category_view),
]

from django.urls import path
from .views import BooksListView, BooksDetailView, BooksCreateView, BooksUpdateView, BooksDeleteView

urlpatterns = [
    path('Books/', BooksListView.as_view(), name='Books-list'),
    path('Books/<int:pk>/', BooksDetailView.as_view(), name='Books-detail'),
    path('Books/create/', BooksCreateView.as_view(), name='Books-create'),
    path('Books/<int:pk>/update/', BooksUpdateView.as_view(), name='Books-update'),
    path('Books/<int:pk>/delete/', BooksDeleteView.as_view(), name='Books-delete'),
]
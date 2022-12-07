from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import Book


class BooksListView(ListView):
    template_name = "Books/Books-list.html"
    model = Book


class BooksDetailView(DetailView):
    template_name = "Books/Books-detail.html"
    model = Book


class BooksCreateView(CreateView):
    template_name = "Books/Books-create.html"
    model = Book
    fields = ['name' ,'purchaser', 'description' ,'author', 'genre']


class BooksUpdateView(UpdateView):
    template_name = "Books/Books-update.html"
    model = Book
    fields = ['name' ,'purchaser', 'description' ,'author', 'genre']


class BooksDeleteView(DeleteView):
    template_name = "Books/Books-delete.html"
    model = Book
    success_url = reverse_lazy("Books-list")
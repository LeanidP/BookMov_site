from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponse, request
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import ListView, TemplateView, CreateView, DetailView

from accounts.forms import LoginUserForm
from .forms import AddPostForm
from .models import *


class index(LoginView):
    form_class = LoginUserForm
    template_name = 'books/login.html'

    def get_success_url(self):
        return reverse_lazy('main')


class SearchResultsView(ListView):
    model = Books
    template_name = 'books/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Books.objects.filter(
            Q(book_title__icontains=query) | Q(author__icontains=query)
        )
        return object_list


def books_list(request):
    posts = Books.objects.all()
    paginator = Paginator(posts, 6)
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)
    return render(request, 'books/main.html', {'page_object': page_object, 'posts': posts})


class ShowPost(DetailView):
    model = Books
    template_name = 'books/post.html'
    pk_url_kwarg = 'post_id'
    context_object_name = 'post'


class AddBooksView(CreateView):
    form_class = AddPostForm
    template_name = 'books/add_books.html'
    success_url = reverse_lazy('main')
    login_url = reverse_lazy('main')
    raise_exception = True


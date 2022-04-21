from django.contrib.auth.views import LoginView
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, CreateView

from accounts.forms import LoginUserForm
from .forms import AddPostForm
from .models import *

menu = [
    {'title': "Мои книги", 'url_name': 'my_books'},
    {'title': "Мои сообщения", 'url_name': 'messages'},
    {'title': "Мои заказы", 'url_name': 'orders'},
    {'title': "Аккаунт", 'url_name': 'account'}
]


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


class HomePageView(TemplateView):
    template_name = 'books/main.html'


class AddBooksView(CreateView):
    form_class = AddPostForm
    template_name = 'books/add_books.html'
    success_url = reverse_lazy('main')
    login_url = reverse_lazy('main')
    raise_exception = True

#    def get_context_data(self, *, object_list=None, **kwargs):
#        context = super().get_context_data(**kwargs)
#        c_def = self.get_user_context(title="Добавление книги")
#        return dict(list(context.items()) + list(c_def.items()))




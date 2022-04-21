from django.urls import path
from django.contrib.auth import views

from accounts.views import RegisterUser, LoginUser, logout_user
from .views import *


urlpatterns = [
    path('', index.as_view(), name='homepage'),
    path('registration/', RegisterUser.as_view(template_name="books/registration.html"), name="registration"),
    path('accounts/login/', LoginUser.as_view(), name='login'),
    path('logout', logout_user, name='logout'),
    path("password_reset/",
         views.PasswordResetView.as_view(template_name="books/password_reset_form.html"), name="password_reset"),
    path("password_reset/done/",
         views.PasswordResetDoneView.as_view(template_name="books/password_reset_done.html"),
         name="password_reset_done"),
    path("reset/<uidb64>/<token>/",
         views.PasswordResetConfirmView.as_view(template_name="books/password_reset_confirm.html"), name="password_reset_confirm"),
    path("reset/done/",
         views.PasswordResetCompleteView.as_view(template_name="books/password_reset_complete.html"), name="password_reset_complete"),
    path('main/', HomePageView.as_view(), name='main'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('add_post/', AddBooksView.as_view(), name='add_post'),


]

from django.test import TestCase
from django.urls import reverse

from books.forms import AddPostForm
from books.models import Books


class BooksTest(TestCase):

    def create_books(self, book_title):
        return Books.objects.create()

    def test_create_books(self):
        B = self.create_books(book_title='book_title')
        self.assertTrue(isinstance(B, Books))

    def test_valid_form(self):
        w = Books.objects.create(
            book_title='book_title',
            book_image='book_image',
            author='author',
            description='description',
            comments='comments',
            user_author='user_author',
            info_author='info_author'
        )
        data = {
            'book_title': w.book_title,
            'book_image': w.book_image,
            'author': w.author,
            'description': w.description,
            'comments': w.comments,
            'user_author': w.user_author,
            'info_author': w.info_author
        }
        form = AddPostForm(data=data)
        self.assertFalse(form.is_valid())

    def test_RegistrationView_Get(self):
        response = self.client.get(reverse('registration'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'books/registration.html')

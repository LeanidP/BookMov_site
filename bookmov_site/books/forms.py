from django import forms
from django.core.exceptions import ValidationError

from books.models import Books


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ['book_title', 'book_image', 'author', 'release_year', 'description', 'rating', 'comments']

    def clean_title(self):
        book_title = self.cleaned_data['book_title']
        if len(book_title) > 200:
            raise ValidationError('Длина превышает 200 символов')

        return book_title

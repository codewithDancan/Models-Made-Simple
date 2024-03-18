from django.contrib import admin
from .models import Book, Author, Borrow, Tag


admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Borrow)
admin.site.register(Tag)

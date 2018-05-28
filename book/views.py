from django.http import HttpResponse
from .models import Book

def index(request):
    all_books = Book.objects.all()
    html = ''
    for book in all_books:
        url = '/book/' + str(book.id) + '/'
        html += '<a href="' + url + '">' + book.title + '</a><br>'
    return HttpResponse(html)

def detail(request, book_id):
    return HttpResponse("<h2>Details for Album id: " + str(book_id) + "</h2>")
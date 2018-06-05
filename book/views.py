from django.shortcuts import render, get_object_or_404
from .models import Book, Question, Answer, Comment


def index(request):
    all_books = Book.objects.all()
    context = {'all_books': all_books}
    return render(request, 'book/index.html', context)

def book(request, book_id):
    # try:
    #     book = Book.objects.get(pk=book_id)
    # except Book.DoesNotExist:
    #     raise Http404("Book does not exist")
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'book/book.html', {'book': book})
    
def ask(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    new_question = Question()
    # change with user id
    new_question.author = "Tomohiro Sato"
    new_question.question = request.POST.get('question')
    new_question.page = int(request.POST.get('page'))
    new_question.like = 0
    new_question.book = book
    try:
        new_question.save()
    except (KeyError, Question.DoesNotExist):
        return render(request, 'book/book.html', {'book': book, 'error_message': "Failed to save question"})
    else:
        return render(request, 'book/book.html', {'book': book})
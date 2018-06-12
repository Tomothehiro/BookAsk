from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Book, Question, Answer, Comment

class IndexView(generic.ListView):
    template_name = 'book/index.html'
    context_object_name = 'all_books'

    def get_queryset(self):
        return Book.objects.all()

class BookView(generic.DetailView):
    model = Book
    fields = ['question', 'page']
    template_name = 'book/book.html'

class AskQuestion(CreateView):
    model = Question

class DetailViewMixin(object):
    details_model = None
    context_detail_object_name = None

    def get_context_data(self, **kwargs):
        context = super(DetailViewMixin, self).get_context_data(**kwargs)
        context[self.context_detail_object_name] = self.get_detail_object()
        return context

    def get_detail_object(self):
        return self.details_model._default_manager.get(pk=self.kwargs['pk'])
    
class CommentCreate(DetailViewMixin, CreateView):
    details_model = Book
    context_detail_object_name = 'post'
    model = Question
    template_name = "book/book.html"
    fields = ['question', 'page']

from django.shortcuts import render, get_object_or_404
# from .models import Book, Question, Answer, Comment


# def index(request):
#     all_books = Book.objects.all()
#     context = {'all_books': all_books}
#     return render(request, 'book/index.html', context)

# def book(request, book_id):
#     # try:
#     #     book = Book.objects.get(pk=book_id)
#     # except Book.DoesNotExist:
#     #     raise Http404("Book does not exist")
#     book = get_object_or_404(Book, pk=book_id)
#     return render(request, 'book/book.html', {'book': book})
    
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
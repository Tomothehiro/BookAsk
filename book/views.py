from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.views import generic
from django.views.generic import View
from django.http import Http404
from .models import Book, Question, Answer, Comment
from .forms import UserForm
from django.contrib import messages
import json
from collections import namedtuple

class IndexView(generic.ListView):
    template_name = 'book/index.html'
    context_object_name = 'all_books'

    def get_queryset(self):
        return Book.objects.all()

class BookView(generic.DetailView):
    model = Book
    template_name = 'book/book.html'

    def get_object(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        book = self.get_object(pk)
        return render(request, self.template_name, {'book': book})

    def post(self, request, pk):
        book = self.get_object(pk)
        new_question = Question()
        # change with user id
        new_question.author = request.user
        new_question.question = request.POST.get('question').encode('utf-8')
        new_question.page = int(request.POST.get('page'))
        new_question.like = 0
        new_question.book = book
        try:
            new_question.save()
        except (KeyError, Question.DoesNotExist):
            return render(request, self.template_name, {'book': book, 'error_message': "Failed to save question"})
        else:
            return render(request, self.template_name, {'book': book})

class QuestionView(generic.DetailView):
    model = Question
    template_name = 'book/question.html'

    def get_object(self, pk):
        try:
            return Question.objects.get(pk=pk)
        except Question.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        question = self.get_object(pk)
        return render(request, self.template_name, {'question': question})

    def post(self, request, pk):
        question = self.get_object(pk)
        new_answer = Answer()
        # change with user id
        new_answer.author = request.user
        new_answer.answer = request.POST.get('answer').encode('utf-8')
        new_answer.like = 0
        new_answer.question = question
        try:
            new_answer.save()
        except (KeyError, Answer.DoesNotExist):
            return render(request, self.template_name, {'question': question, 'error_message': "Failed to save answer"})
        else:
            return render(request, self.template_name, {'question': question})

class UserFormView(View):
    form_class = UserForm
    template_name = 'registration/login.html'

    # display blank form for GET request
    def get(self, request):
        form = self.form_class(None)
        return redirect('/accounts/login/#register')
        # return render(request, self.template_name, {'form': form})

    # register the user for POST request
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            # creates object from the form, but not save it the the DB
            user = form.save(commit=False)

            # cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # returns User objects if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('book:index')
        
        x = json.loads(form.errors.as_json(), object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
        for attr, value in x.__dict__.iteritems():
            for x in value:
                if attr == 'username':
                    messages.warning(request, x.message)
                elif attr == 'password':
                    messages.error(request, x.message)
                elif attr == 'email':
                    messages.info(request, x.message)
        
        return redirect('/accounts/login/#register')



# from .models import Category


# def index(request):
#     all_books = Book.objects.all()
#     context = {'all_books': all_books}
#     return render(request, 'book/index.html', context)

# def seed(request):
#     category = Category()
#     category.name = "Science"
#     category.save()

#     book = Book()
#     book.isbn13 = "9781464183393"
#     book.title = "Molecular Cell Biology"
#     book.author = "Harvey Lodish"
#     book.category = category
#     book.cover = "9781464183393_l.jpg"
#     book.save()

#     return render(request, 'book/book.html', {'book': book})
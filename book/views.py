from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.db.models import Q
from django.views import generic
from django.views.generic import View
from django.http import Http404, HttpResponse
from .models import Category, Book, Question, Answer, AnswerComment, QuestionComment, QuestionLike
from .forms import UserForm
from django.contrib import messages
import json
from collections import namedtuple

class IndexView(generic.ListView):
    template_name = 'book/index.html'

    def get_category_object(self):
        try:
            return Category.objects.all()
        except Category.DoesNotExist:
            raise Http404

    # get: get all book
    def get(self, request):
        query = request.GET.get('q', '')
        cid = request.GET.get('c', '')
        # TODO: retrieve only the first 20~30
        if cid:
            books = Book.objects.filter(category_id=cid)
        elif query:
            books = Book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query))
        else:
            books = Book.objects.all()
        categories = self.get_category_object()
        return render(request, self.template_name, {'books': books, 'categories': categories, 'query':query, 'cid': cid})

class BookView(generic.DetailView):
    model = Book
    template_name = 'book/book.html'

    def get_object(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            raise Http404

    # get: get book with asked questions
    def get(self, request, pk):
        book = self.get_object(pk)
        return render(request, self.template_name, {'book': book})

    # post: save new question for a book
    def post(self, request, pk):
        book = self.get_object(pk)
        new_question = Question()
        # change with user id
        new_question.author = request.user
        new_question.question = request.POST.get('question').encode('utf-8')
        new_question.page = int(request.POST.get('page'))
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

    def get_question_object(self, id):
        try:
            return Question.objects.get(pk=id)
        except Question.DoesNotExist:
            raise Http404

    # get like count for a question
    def get_questionLike_object(self, question, user):
        try:
            questionLike = QuestionLike.objects.get(question=question, user=user)
            return questionLike
        except QuestionLike.DoesNotExist:
            return None

    # get: get a question with answers
    def get(self, request, pk, id):
        question = self.get_question_object(id)
        if request.user.is_authenticated():
           questionLike = self.get_questionLike_object(question, request.user)
        else:
            questionLike = None
        return render(request, self.template_name, {'question': question, 'questionLike': questionLike})

    # post: save new answer to a question
    def post(self, request, pk, id):
        question = self.get_question_object(id)
        new_answer = Answer()
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

# Like Class for Questions
class QuestionLikeView(generic.DetailView):
    model = QuestionLike
    question = None

    def get_object(self, id, user):
        try:
            self.question = Question.objects.get(pk=id)
            questionLike = QuestionLike.objects.get(question=self.question, user=user)
            return questionLike
        except QuestionLike.DoesNotExist:
            return None

    def save_object(self, id, user):
        
        new_questionLike = QuestionLike()
        new_questionLike.question = self.question
        new_questionLike.user = user
        try:
            new_questionLike.save()
        except (KeyError, QuestionLike.DoesNotExist):
            return None
        else:
            return new_questionLike

    def get(self, request, pk, id):
        if not request.user.is_authenticated():
            return HttpResponse(0)
        questionLike = self.get_object(id, request.user)
        if questionLike is None:
            result = self.save_object(id, request.user)
            if result is None:
                return HttpResponse(0) #Return Fail to add Like
            else:
                return HttpResponse(1) #Return Success
        else:
            return HttpResponse(0) #Return Fail to add Like

    def delete(self, request, pk, id):
        if not request.user.is_authenticated():
            return HttpResponse(0)
        questionLike = self.get_object(id, request.user)
        if questionLike is not None:
            result = questionLike.delete() # successful delete will return (1, {u'book.QuestionLike': 1})
            if result[0] == 1:
                return HttpResponse(1) #Return Success
            else:
                return HttpResponse(0) #Return Fail to Unlike
        else:
            return HttpResponse(0) #Return Fail to Unlike, no Like found

class QuestionCommentView(generic.DetailView):
    model = QuestionComment
    question = None

    def get_question(self, id):
        try:
            return Question.objects.get(pk=id)
        except QuestionComment.DoesNotExist:
            # TODO: return exception
            return None

    def save_object(self, id, user):
        try:
            new_questionLike.save()
        except (KeyError, QuestionLike.DoesNotExist):
            return None
        else:
            return new_questionLike

    def post(self, request, pk, id, comid):
        # TODO: Update comment if comid > 0
        if not request.user.is_authenticated():
            return HttpResponse(0)
        comment = QuestionComment()
        comment.comment = request.POST.get('comment')
        comment.author = request.user
        comment.question = self.get_question(id)
        try:
            comment.save()
            return HttpResponse(1)
        except (KeyError, QuestionComment.DoesNotExist):
            return HttpResponse(0)

    def delete(self, request, pk, id, comid):
        if not request.user.is_authenticated():
            return HttpResponse(0)
        # TODO: delete comment


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
# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Book, Category, Question, Answer, AnswerComment, QuestionComment, QuestionLike, Watch

admin.site.register(Book)
admin.site.register(Category)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(AnswerComment)
admin.site.register(QuestionComment)
admin.site.register(QuestionLike)
admin.site.register(Watch)
# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Book, Category, Question, Answer, Comment, Like, Watch

admin.site.register(Book)
admin.site.register(Category)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Watch)
# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Book, Question, Answer

admin.site.register(Book)
admin.site.register(Question)
admin.site.register(Answer)
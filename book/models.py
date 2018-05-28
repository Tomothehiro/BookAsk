# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    category = models.CharField(max_length=100)
    cover = models.CharField(max_length=1000)

class Question(models.Model):
    author = models.CharField(max_length=250)
    question = models.CharField(max_length=4000)
    #date = models.
    page = models.PositiveIntegerField()

    def __str__(self):
        return self.author + ' - ' + str(self.page) + ' - ' + self.question

class Answer(models.Model):
    author = models.CharField(max_length=250)
    answer = models.CharField(max_length=4000)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.author + ' - ' + str(self.question) + ' - ' + self.answer
    
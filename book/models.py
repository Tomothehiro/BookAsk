from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=250)

    def __unicode__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    cover = models.FileField()

    def get_absolute_url(self):
        return reverse('book:book', kwargs={'pk': self.pk})

    def __unicode__(self):
        return self.title

class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.CharField(max_length=4000)
    #date = models.
    page = models.PositiveIntegerField()
    like = models.PositiveIntegerField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('book:book', kwargs={'pk': self.pk})

    def __unicode__(self):
        return self.question

class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    answer = models.CharField(max_length=4000)
    like = models.PositiveIntegerField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.answer

class Comment(models.Model):
    author = models.CharField(max_length=250)
    comment = models.CharField(max_length=4000)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.comment

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.book

class Watch(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    
    def __unicode__(self):
        return self.book
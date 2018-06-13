from django.db import models
from django.core.urlresolvers import reverse

class Book(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    category = models.CharField(max_length=100)
    cover = models.FileField()

    def get_absolute_url(self):
        return reverse('book:book', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title + ' - ' + self.author

class Question(models.Model):
    author = models.CharField(max_length=250)
    question = models.CharField(max_length=4000)
    #date = models.
    page = models.PositiveIntegerField()
    like = models.PositiveIntegerField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('book:book', kwargs={'pk': self.pk})

    def __str__(self):
        return self.author + ' - ' + str(self.page) + ' - ' + self.question

class Answer(models.Model):
    author = models.CharField(max_length=250)
    answer = models.CharField(max_length=4000)
    like = models.PositiveIntegerField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.author + ' - ' + str(self.question) + ' - ' + self.answer

class Comment(models.Model):
    author = models.CharField(max_length=250)
    comment = models.CharField(max_length=4000)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)

# class Like(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     book = models.ForeignKey(Book, on_delete=models.CASCADE)
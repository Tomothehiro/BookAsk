from django.conf.urls import url
from . import views

app_name = 'book'

urlpatterns = [
    # /book/
    url(r'^$', views.IndexView.as_view(), name='index'),

    # /book/register/
    url(r'^register/$', views.UserFormView.as_view(), name='register'),

    # /book/1234567890123/
    url(r'^(?P<pk>[0-9a-zA-Z]+)/$', views.BookView.as_view(), name='book'),

    # /book/1234567890123/q/1/
    url(r'^(?P<pk>[0-9a-zA-Z]+)/q/(?P<id>[0-9]+)/$', views.QuestionView.as_view(), name='question'),

    # /book/1234567890123/q/1/like
    url(r'^(?P<pk>[0-9a-zA-Z]+)/q/(?P<id>[0-9]+)/like/$', views.QuestionLikeView.as_view(), name='question-like'),

    # /book/1234567890123/q/1/comment
    url(r'^(?P<pk>[0-9a-zA-Z]+)/q/(?P<id>[0-9]+)/comment/(?P<comid>[0-9]+)/$', views.QuestionCommentView.as_view(), name='question-comment'),
]

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

    # /book/1234567890123/q/1
    url(r'^(?P<pk>[0-9a-zA-Z]+)/q/$', views.QuestionView.as_view(), name='question'),
]

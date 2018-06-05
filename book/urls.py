from django.conf.urls import url
from . import views

app_name = 'book'

urlpatterns = [
    # /book/
    url(r'^$', views.index, name='index'),

    # /book/71/
    url(r'^(?P<book_id>[0-9a-zA-Z]+)/$', views.book, name='book'),

    # /book/ask/
    url(r'^(?P<book_id>[0-9a-zA-Z]+)/ask/$', views.ask, name='ask'),
]

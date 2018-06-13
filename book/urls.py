from django.conf.urls import url
from . import views

app_name = 'book'

urlpatterns = [
    # /book/
    url(r'^$', views.IndexView.as_view(), name='index'),

    # /book/71/
    url(r'^(?P<pk>[0-9a-zA-Z]+)/$', views.BookView.as_view(), name='book'),

    # /book/71/q/
    url(r'^(?P<book_id>[0-9a-zA-Z]+)/q/$', views.ask, name='q'),
]

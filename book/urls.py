from django.conf.urls import url
from . import views

urlpatterns = [
    # /book/
    url(r'^$', views.index, name='index'),

    # /book/71/
    url(r'^(?P<book_id>[0-9a-zA-Z]+)/$', views.detail, name='detail'),
]

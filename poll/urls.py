from django.urls import path, re_path
from . import views
urlpatterns = [
    # ex : /poll/
    path('poll/', views.index, name='index'),
    # ex : /poll/1/
    path('poll/<int:question_id>/', views.detail, name='detail'),
    # ex : /poll/1/results/
    path('poll/<int:question_id>/results/', views.results, name='results'),
    # ex : /poll/1/vote
    re_path(r'^poll/(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    path('vote/<int:question_id>/<int:index>/', views.votes, name='votes'),
]


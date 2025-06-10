from django.urls import path
from . import views

app_name = "polls"

urlpatterns = [

    # CBV URLs
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
    # CRUD URLs
    path("create/", views.QuestionCreateView.as_view(), name="question_create"),
    path("<int:pk>/update/", views.QuestionUpdateView.as_view(), name="question_update"),
    path("<int:pk>/delete/", views.QuestionDeleteView.as_view(), name="question_delete"),

    path('questions/', views.question_list, name='question_list'), #127.0.0.1:8000/polls/questions/
]

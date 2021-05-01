from django.urls import path, include

from .views import AskAPIView, ask_question

app_name = 'albert'

urlpatterns = [
    path("ask/", ask_question, name="ask"),
    path("ask/api", AskAPIView.as_view(), name="ask_api"),
]
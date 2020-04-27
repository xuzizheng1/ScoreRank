
from django.urls import path

from rank.views import RankView, InputView

urlpatterns = [
    path('', InputView.as_view()),
    path('rank/', RankView.as_view()),
]

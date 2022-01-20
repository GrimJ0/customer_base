from django.urls import path

from .views import HomeList, NewClientView

urlpatterns = [
    path("", HomeList.as_view(), name="home"),
    path("new/", NewClientView.as_view(), name="new")
]
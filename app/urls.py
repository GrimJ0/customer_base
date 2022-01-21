from django.urls import path

from .views import HomeList, NewClientView, RemoveClientView

urlpatterns = [
    path("", HomeList.as_view(), name="home"),
    path("new/", NewClientView.as_view(), name="new"),
    path("remove/<int:id>/", RemoveClientView.as_view(), name="remove_client")
]
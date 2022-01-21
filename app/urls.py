from django.urls import path

from .views import HomeList, NewClientView, EditRecipeView, RemoveClientView

urlpatterns = [
    path("", HomeList.as_view(), name="home"),
    path("new/", NewClientView.as_view(), name="new"),
    path("edit/<int:id>/", EditRecipeView.as_view(), name="edit_client"),
    path("remove/<int:id>/", RemoveClientView.as_view(), name="remove_client"),
]
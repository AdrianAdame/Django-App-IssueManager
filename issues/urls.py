from django.urls import path
from issues import views

urlpatterns = [
    path("", views.IssueListView.as_view(), name="list"),
    path("<int:pk>/", views.IssueDetailView.as_view(), name="detail"),
    path("<int:pk>/update/", views.IssueUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", views.IssueDeleteView.as_view(), name="delete"),
    path("new/", views.IssueCreateView.as_view(), name="new")
]
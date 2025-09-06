from django.urls import path
from . import views

urlpatterns = [
    path("viewer/", views.viewer, name="viewer"),
    path("admin/", views.admin_page, name="admin"),
    path("api/state/", views.get_state, name="get_state"),
    path("api/update-teams/", views.update_teams, name="update_teams"),
    path("api/control-timer/", views.control_timer, name="control_timer"),
]

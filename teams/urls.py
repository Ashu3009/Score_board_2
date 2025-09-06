from django.urls import path
from . import views

urlpatterns = [
    path("viewer/", views.viewer, name="teams_viewer"),
    path("admin/", views.admin_page, name="teams_admin"),

    # APIs
    path("update_name/<str:team>/", views.update_name, name="update_name"),
    path("update_score/<str:team>/<str:action>/", views.update_score, name="update_score"),
    path("reset_score/", views.reset_score, name="reset_score"),
]

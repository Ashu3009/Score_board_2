from django.urls import path
from . import views

urlpatterns = [
    path("admin/", views.admin_page, name="rpg_admin"),
    path("viewer/", views.viewer_page, name="rpg_viewer"),
    path("get_state/", views.get_state, name="rpg_get_state"),
]

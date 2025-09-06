from django.urls import path
from . import views

urlpatterns = [
    path("admin/", views.admin_page, name="final_admin"),
    path("viewer/", views.viewer_page, name="final_viewer"),
    path("get_state/", views.get_state, name="final_get_state"),
]

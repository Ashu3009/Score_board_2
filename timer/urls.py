from django.urls import path
from . import views

urlpatterns = [
    path("admin-timer/", views.admin_page, name="admin_page"),
    path("viewer/", views.viewer_page, name="viewer_page"),

    path("start/", views.start_timer, name="start_timer"),
    path("pause/", views.pause_timer, name="pause_timer"),
    path("reset/", views.reset_timer, name="reset_timer"),
    path("get_timer/", views.get_timer, name="get_timer"),
]


from django.urls import path
from . import views

urlpatterns = [
    path("admin/", views.admin_page, name="admin_page"),
    path("viewer/", views.viewer_page, name="viewer_page"),

    # Main timer
    path("start_main/", views.start_main),
    path("pause_main/", views.pause_main),
    path("reset_main/", views.reset_main),

    # Penalty timer
    path("start_penalty/", views.start_penalty),
    path("pause_penalty/", views.pause_penalty),
    path("reset_penalty/", views.reset_penalty),

    # Score update
    path("update_score/<str:team>/<int:delta>/", views.update_score),

    # Round (manual, independent)
    path("next_round/", views.next_round),

    # Timer fetch (main + penalty + score + round)
    path("get_timer/", views.get_timer),
]

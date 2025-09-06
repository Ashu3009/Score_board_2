from django.urls import path
from . import views

urlpatterns = [
    path("admin/", views.admin_page, name="admin_page_4"),
    path("viewer/", views.viewer_page, name="viewer_page_4"),

    # team name
    path("update_team_name/<str:team>/<str:name>/", views.update_team_name),

    # score
    path("update_score/<str:team>/<int:delta>/", views.update_score),

    # round
    path("next_round/", views.next_round),

    # timers
    path("start_main/", views.start_main),
    path("pause_main/", views.pause_main),
    path("reset_main/", views.reset_main),

    path("start_penalty/", views.start_penalty),
    path("pause_penalty/", views.pause_penalty),
    path("reset_penalty/", views.reset_penalty),

    # fetch
    path("get_timer/", views.get_timer),
]

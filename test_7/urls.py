from django.urls import path
from . import views

urlpatterns = [
    path('admin-panel/', views.admin_view, name='admin_panel'),
    path('viewer/', views.viewer_view, name='viewer'),
    path('winner/', views.winner_view, name='winner'),
    path('video/', views.video_view, name='video'),
    path('api/set-display/', views.set_display, name='set_display'),
    path('api/get-display/', views.get_display, name='get_display'),
]

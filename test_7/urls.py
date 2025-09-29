from django.urls import path
from . import views

urlpatterns = [
    path('admin/', views.admin_view, name='admin'),
    path('viewer/', views.viewer_view, name='viewer'),
    path("video/", views.video_page, name="video"),
    # path("set_mode/<str:mode>/", views.set_mode, name="set_mode"),
]

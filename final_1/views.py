import json
import os
from django.http import JsonResponse
from django.shortcuts import render
from django.conf import settings

# JSON file paths
STATE_FILE = os.path.join(settings.BASE_DIR, "final_1", "state.json")
TIMERS_FILE = os.path.join(settings.BASE_DIR, "final_1", "timers.json")


# -------- Helper Functions --------
def load_json(path, default_data):
    """Agar file hai to load karo, warna default data create karo"""
    if not os.path.exists(path):
        save_json(path, default_data)
        return default_data
    with open(path, "r") as f:
        return json.load(f)


def save_json(path, data):
    """Data ko JSON file me save karega"""
    with open(path, "w") as f:
        json.dump(data, f)


# -------- Default States --------
DEFAULT_STATE = {
    "team1_name": "Team 1",
    "team2_name": "Team 2",
    "team1_score": 0,
    "team2_score": 0,
    "round": 1,
}

DEFAULT_TIMERS = {
    "game_timer": 180,     # 3 minutes
    "penalty_timer": 10,   # 10 sec
    "running": False,
}


# -------- Views --------
def admin_page(request):
    """Custom admin page"""
    return render(request, "final_1/admin.html")


def viewer_page(request):
    """Viewer page"""
    return render(request, "final_1/viewer.html")


def get_state(request):
    """Ajax call ke liye: dono JSON merge karke bhejo"""
    state = load_json(STATE_FILE, DEFAULT_STATE)
    timers = load_json(TIMERS_FILE, DEFAULT_TIMERS)

    # Merge both dicts
    combined = {**state, **timers}
    return JsonResponse(combined)


# (Optional) agar alag se chahiye ho to static aur dynamic ke endpoints bana lo:

def get_static_state(request):
    state = load_json(STATE_FILE, DEFAULT_STATE)
    return JsonResponse(state)


def get_dynamic_state(request):
    timers = load_json(TIMERS_FILE, DEFAULT_TIMERS)
    return JsonResponse(timers)

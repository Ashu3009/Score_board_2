import json
import os
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

STATE_FILE = os.path.join(os.path.dirname(__file__), "state.json")

def load_state():
    with open(STATE_FILE, "r") as f:
        return json.load(f)

def save_state(state):
    with open(STATE_FILE, "w") as f:
        json.dump(state, f)

# Viewer page
def viewer(request):
    state = load_state()
    return render(request, "test_2/viewer.html", {"state": state})

# Admin page
def admin_page(request):
    state = load_state()
    return render(request, "test_2/admin.html", {"state": state})

# API - get state
def get_state(request):
    return JsonResponse(load_state())

# API - update team names
@csrf_exempt
def update_teams(request):
    if request.method == "POST":
        state = load_state()
        red = request.POST.get("team_red_name")
        blue = request.POST.get("team_blue_name")
        if red: state["team_red_name"] = red
        if blue: state["team_blue_name"] = blue
        save_state(state)
    return JsonResponse(state)

# API - timer control
@csrf_exempt
def control_timer(request):
    if request.method == "POST":
        state = load_state()
        action = request.POST.get("action")

        if action == "start":
            state["game_running"] = True
        elif action == "stop":
            state["game_running"] = False
        elif action == "reset":
            state["game_time"] = 180
            state["game_running"] = False
        elif action == "update_time":   # countdown update from admin JS
            new_time = request.POST.get("game_time")
            if new_time is not None:
                state["game_time"] = int(new_time)

        save_state(state)
        return JsonResponse(state)

    return JsonResponse({"error": "Invalid request"})

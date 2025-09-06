import os
import json
import time
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.conf import settings

# JSON state file ka path
STATE_FILE = os.path.join(settings.BASE_DIR, "round_penality_game_timer", "state.json")


def load_state():
    with open(STATE_FILE, "r") as f:
        return json.load(f)


def save_state(state):
    with open(STATE_FILE, "w") as f:
        json.dump(state, f)


# helper: remaining time calculate karna
def get_remaining_time(timer_data):
    if timer_data["running"] and timer_data["start_time"]:
        elapsed = int(time.time() - timer_data["start_time"])
        remaining = timer_data["duration"] - elapsed
        return max(0, remaining)
    return timer_data["duration"]


def admin_page(request):
    state = load_state()

    if request.method == "POST":
        # Game Timer Controls
        if "start_game" in request.POST:
            state["game_timer"]["start_time"] = time.time()
            state["game_timer"]["running"] = True
        elif "stop_game" in request.POST:
            state["game_timer"]["running"] = False
        elif "reset_game" in request.POST:
            state["game_timer"]["duration"] = 180
            state["game_timer"]["start_time"] = None
            state["game_timer"]["running"] = False

        # Penalty Timer Controls
        elif "start_penalty" in request.POST:
            state["penalty_timer"]["start_time"] = time.time()
            state["penalty_timer"]["running"] = True
        elif "reset_penalty" in request.POST:
            state["penalty_timer"]["duration"] = 10
            state["penalty_timer"]["start_time"] = None
            state["penalty_timer"]["running"] = False

        # Round Controls
        elif "next_round" in request.POST:
            state["round"] += 1
        elif "prev_round" in request.POST and state["round"] > 1:
            state["round"] -= 1

        # Team Names
        elif "update_teams" in request.POST:
            state["team1_name"] = request.POST.get("team1_name", state["team1_name"])
            state["team2_name"] = request.POST.get("team2_name", state["team2_name"])

        # Team Scores
        elif "update_scores" in request.POST:
            state["team1_score"] = int(request.POST.get("team1_score", state["team1_score"]))
            state["team2_score"] = int(request.POST.get("team2_score", state["team2_score"]))

        save_state(state)
        return redirect("rpg_admin")

    return render(request, "rpg/admin.html", {"state": state})


def viewer_page(request):
    state = load_state()
    return render(request, "rpg/viewer.html", {"state": state})


def get_state(request):
    state = load_state()
    # timers ke liye live remaining add kar rahe
    state["game_timer"]["remaining"] = get_remaining_time(state["game_timer"])
    state["penalty_timer"]["remaining"] = get_remaining_time(state["penalty_timer"])
    return JsonResponse(state)

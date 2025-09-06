import json, os
from django.shortcuts import render
from django.http import JsonResponse

TIMER_FILE = os.path.join(os.path.dirname(__file__), "timer.json")

def read_data():
    with open(TIMER_FILE, "r") as f:
        return json.load(f)

def write_data(data):
    with open(TIMER_FILE, "w") as f:
        json.dump(data, f)

# Pages
def admin_page(request):
    return render(request, "test_4/admin.html")

def viewer_page(request):
    return render(request, "test_4/viewer.html")

# Team name update
def update_team_name(request, team, name):
    data = read_data()
    if team == "red":
        data["team_red_name"] = name
    elif team == "blue":
        data["team_blue_name"] = name
    write_data(data)
    return JsonResponse({"status": "team_name_updated"})

# Score update
def update_score(request, team, delta):
    data = read_data()
    if team == "red":
        data["team_red_score"] += delta
    elif team == "blue":
        data["team_blue_score"] += delta
    write_data(data)
    return JsonResponse({"status":"score_updated"})

# Round
def next_round(request):
    data = read_data()
    data["round"] += 1
    write_data(data)
    return JsonResponse({"status":"next_round"})

# Timers
def start_main(request):
    data = read_data()
    data["is_main_running"] = True
    write_data(data)
    return JsonResponse({"status": "started"})

def pause_main(request):
    data = read_data()
    data["is_main_running"] = False
    write_data(data)
    return JsonResponse({"status": "paused"})

def reset_main(request):
    data = read_data()
    data["main_timer"] = 180
    data["is_main_running"] = False
    write_data(data)
    return JsonResponse({"status": "reset"})

def start_penalty(request):
    data = read_data()
    if data["penalty_timer"] == 0:
        data["penalty_timer"] = 10
    data["is_penalty_running"] = True
    write_data(data)
    return JsonResponse({"status": "penalty_started"})

def pause_penalty(request):
    data = read_data()
    data["is_penalty_running"] = False
    write_data(data)
    return JsonResponse({"status": "penalty_paused"})

def reset_penalty(request):
    data = read_data()
    data["penalty_timer"] = 0
    data["is_penalty_running"] = False
    write_data(data)
    return JsonResponse({"status": "penalty_reset"})

# Fetch data
def get_timer(request):
    data = read_data()

    # Main timer
    if data["is_main_running"] and data["main_timer"] > 0:
        data["main_timer"] -= 1
        if data["main_timer"] <= 0:
            data["main_timer"] = 0
            data["is_main_running"] = False

    # Penalty timer
    if data["is_penalty_running"] and data["penalty_timer"] > 0:
        data["penalty_timer"] -= 1
        if data["penalty_timer"] <= 0:
            data["penalty_timer"] = 0
            data["is_penalty_running"] = False

    write_data(data)
    return JsonResponse(data)

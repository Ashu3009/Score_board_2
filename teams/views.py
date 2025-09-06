import json
from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
import os

# JSON file ka path
JSON_PATH = os.path.join(settings.BASE_DIR, "teams", "teams.json")

def load_data():
    with open(JSON_PATH, "r") as f:
        return json.load(f)

def save_data(data):
    with open(JSON_PATH, "w") as f:
        json.dump(data, f, indent=4)

# Viewer page
def viewer(request):
    data = load_data()
    return render(request, "teams/viewer.html", {"teams": data})

# Admin page
def admin_page(request):
    data = load_data()
    return render(request, "teams/admin.html", {"teams": data})

# API: update team name
def update_name(request, team):
    if request.method == "POST":
        data = load_data()
        new_name = request.POST.get("name")
        if team in data and new_name:
            data[team]["name"] = new_name
            save_data(data)
        return JsonResponse(data)

# API: update score (+1 or -1)
def update_score(request, team, action):
    data = load_data()
    if team in data:
        if action == "inc":
            data[team]["score"] += 1
        elif action == "dec":
            data[team]["score"] -= 1
        save_data(data)
    return JsonResponse(data)

# API: reset score
def reset_score(request):
    data = load_data()
    data["team1"]["score"] = 0
    data["team2"]["score"] = 0
    save_data(data)
    return JsonResponse(data)

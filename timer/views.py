import json, os
from django.http import JsonResponse
from django.shortcuts import render

TIMER_FILE = os.path.join(os.path.dirname(__file__), "timer.json")

def read_timer():
    with open(TIMER_FILE, "r") as f:
        return json.load(f)

def write_timer(data):
    with open(TIMER_FILE, "w") as f:
        json.dump(data, f)

def admin_page(request):
    return render(request, "timer/admin.html")

def viewer_page(request):
    return render(request, "timer/viewer.html")


def start_timer(request):
    data = read_timer()
    data["is_running"] = True
    write_timer(data)
    return JsonResponse({"status": "started"})

def pause_timer(request):
    data = read_timer()
    data["is_running"] = False
    write_timer(data)
    return JsonResponse({"status": "paused"})

def reset_timer(request):
    data = {"remaining_time": 180, "is_running": False}
    write_timer(data)
    return JsonResponse({"status": "reset"})

def get_timer(request):
    data = read_timer()
    if data["is_running"] and data["remaining_time"] > 0:
        data["remaining_time"] -= 1
        if data["remaining_time"] <= 0:
            data["remaining_time"] = 0
            data["is_running"] = False
        write_timer(data)
    return JsonResponse({"time": data["remaining_time"]})
